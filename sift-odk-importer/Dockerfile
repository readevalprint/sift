FROM ubuntu

ADD requirements.txt /code/requirements.txt
ADD apt-packages.txt /code/apt-packages.txt

RUN apt-get update -qq && apt-get install -y wget lsb-release gnupg2
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
RUN wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - |  apt-key add -

RUN apt-get update -qq && apt-get install -y wget

RUN cat /code/apt-packages.txt 
RUN cat /code/apt-packages.txt | xargs apt-get --yes --force-yes install
RUN pip3 install virtualenv

RUN virtualenv -p python3 /var/env/
RUN /var/env/bin/pip install -r /code/requirements.txt

WORKDIR /code

ADD ./ /code/

ENTRYPOINT ["bash", "/code/entrypoint.sh"]
CMD ["manage", "runserver", "0.0.0.0:8843"]
