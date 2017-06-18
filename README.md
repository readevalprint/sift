# Gather2

> Survey collection and analytics

[![Build Status](https://travis-ci.org/readevalprint/sift.svg?branch=master)](https://travis-ci.org/readevalprint/sift)

## Setup

### Dependencies

- git
- [docker-compose](https://docs.docker.com/compose/)

### Installation

```
$ git clone git@github.com:readevalprint/sift.git
$ cd sift

$ docker-compose build
$ docker-compose run core setuplocaldb
$ docker-compose run odk-importer setuplocaldb
```

### Setup

The only thing that you need now is a superuser!
```
docker-compose run core manage createsuperuser
docker-compose run odk-importer manage createsuperuser
```

## Usage

This will start the sift-core 0.0.0.0:8000 and the odk-importer on 0.0.0.0:8443


```
$ docker-compose up
```

## Development

All development should be tested within the container, but developed in the host folder. Read the `docker-compose.yml` file to see how it's mounted.
```
$ docker-compose run core bash
root@localhost:/#
```

## Deployment


When deploying set the env var `DJANGO_S3_FILE_STORAGE` to True. See `settings.py` for the other available settings.

Infrastructure deployment is done with AWS CloudFormation, which configuration files are stored in [cloudformation](cloudformation) directory.

Application deployment is managed by AWS Beanstalk and is being done automatically on the following branches/environments:

All the logs are forwarded to CloudWatch Logs to be easily accessible for developers
