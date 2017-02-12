FROM ubuntu:14.04

COPY /src /opt/managerapp/

RUN apt-get update
RUN apt-get install -y build-essential python3-dev python3-pip

run pip3 install -r /opt/managerapp/requirements.txt

EXPOSE 5000
WORKDIR /opt/managerapp
