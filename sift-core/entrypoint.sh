#!/bin/bash
set -e
set -x


# Define help message
show_help() {
    echo """
    Commands
    manage        : Invoke django manage.py commands
    setuplocaldb  : Create empty database for sift core
    setupproddb   : Create empty database for production
    test_coverage : runs tests with coverage output
    start         : start webserver behind nginx (prod for serving static files)
    pip_freeze    : freeze pip dependencies and write to requirements.txt
    """
}

setup_local_db() {
    set +e
    cd /code/
    /var/env/bin/python manage.py sqlcreate | psql -U $RDS_USERNAME -h $RDS_HOSTNAME
    set -e
    /var/env/bin/python manage.py migrate
}

setup_prod_db() {
    set +e
    cd /code/
    set -e
    /var/env/bin/python manage.py migrate
}

setup_logs_forwarding() {
    local logfiles="${*}"
    for logfile in ${logfiles}; do
       cat >> /var/awslogs/etc/awslogs.conf <<EOF
[${logfile}]
file = ${logfile}
log_stream_name = ${PROJECT_NAME}/${logfile}/$(hostname)
initial_position = start_of_file
log_group_name = ${DEPLOY_ENV}
EOF
    done
}

pip_freeze() {
    virtualenv -p python3 /tmp/env/
    /tmp/env/bin/pip install -r ./primary-requirements.txt --upgrade
    set +x
    echo -e "###\n# frozen requirements DO NOT CHANGE\n# To update this update 'primary-requirements.txt' then run ./entrypoint.sh pip_freeze\n###" | tee requirements.txt
    /tmp/env/bin/pip freeze | tee -a requirements.txt
}

case "$1" in
    manage )
        cd /code/
        /var/env/bin/python manage.py "${@:2}"
    ;;
    setuplocaldb )
        setup_local_db
    ;;
    setupproddb )
        setup_prod_db
    ;;
    test_coverage)
        source /var/env/bin/activate
        coverage run --rcfile="/code/.coveragerc" /code/manage.py test core "${@:2}"
        coverage annotate --rcfile="/code/.coveragerc"
        coverage report --rcfile="/code/.coveragerc"
        cat << "EOF"
  ____                 _     _       _     _
 / ___| ___   ___   __| |   (_) ___ | |__ | |
| |  _ / _ \ / _ \ / _` |   | |/ _ \| '_ \| |
| |_| | (_) | (_) | (_| |   | | (_) | |_) |_|
 \____|\___/ \___/ \__,_|  _/ |\___/|_.__/(_)
                          |__/

EOF
    ;;
    start )
        cd /code/
        setup_prod_db
        /var/env/bin/python manage.py collectstatic --noinput
        /usr/local/bin/supervisord -c /etc/supervisor/supervisord.conf
        setup_logs_forwarding "/var/log/uwsgi/uwsgi.log"
        nginx -g "daemon off;"
    ;;
    pip_freeze )
        pip_freeze
    ;;
    bash )
        bash "${@:2}"
    ;;
    help)
        show_help
    ;;
    *)
        show_help
    ;;
esac
