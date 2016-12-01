FROM ubuntu:14.04

COPY /src /opt/oauth-api/

RUN apt-get update
RUN apt-get install -y build-essential python3-dev python3-pip

run pip3 install -r /opt/oauth-api/requirements.txt

EXPOSE 80
WORKDIR /opt/oauth-api
