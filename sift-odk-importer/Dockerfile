FROM ubuntu:16.04

ADD requirements.txt /code/requirements.txt
ADD apt-packages.txt /code/apt-packages.txt

RUN apt-get update -qq && apt-get install -y wget

RUN cat /code/apt-packages.txt 
RUN cat /code/apt-packages.txt | xargs apt-get --yes --force-yes install
RUN pip3 install virtualenv

RUN virtualenv -p python3 /var/env/
RUN /var/env/bin/pip install -r /code/requirements.txt

WORKDIR /code

ADD ./ /code/

ENTRYPOINT ["bash", "/code/entrypoint.sh"]
CMD ["manage", "runserver", "0.0.0.0:8443"]
