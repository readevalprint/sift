FROM ubuntu:latest

ENV TERM screen-256color


RUN apt-get update -qq && apt-get install -y wget lsb-release gnupg2
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
RUN wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - |  apt-key add -


ADD conf/apt-packages.txt /code/conf/apt-packages.txt
RUN apt-get update -qq && cat /code/conf/apt-packages.txt | xargs apt-get -qq --yes --force-yes install

ADD requirements.txt /code/requirements.txt
RUN pip3 install virtualenv pip --upgrade

RUN virtualenv -p python3 /var/env/
RUN /var/env/bin/pip install -r /code/requirements.txt

WORKDIR /code/

COPY ./ /code

ENTRYPOINT ["bash", "/code/entrypoint.sh"]
CMD ["manage", "runserver", "0.0.0.0:8000"]
