FROM ubuntu:20.04

# linux updates and installs
RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get update
RUN apt-get install -y vim
RUN apt-get install -y curl 
# RUN curl -sSL https://get.docker.com/ | sh
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get update
RUN apt-get install -y python-dev default-libmysqlclient-dev
RUN apt-get install -y python3-dev
RUN apt-get install -y zip
RUN apt-get install -y unzip
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install
RUN apt-get update
RUN rm awscliv2.zip
RUN rm -r aws

RUN mkdir /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip3 install -r /usr/src/app/requirements.txt
RUN rm -r /usr/src/app
