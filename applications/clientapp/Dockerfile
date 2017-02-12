FROM ubuntu:14.04

COPY /src /opt/clientapp/

ENV SECRET_KEY you-will-never-guess

RUN apt-get update
RUN apt-get install -y build-essential python3-dev python3-pip

run pip3 install -r /opt/clientapp/requirements.txt



EXPOSE 80
WORKDIR /opt/clientapp
