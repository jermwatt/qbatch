FROM python:3.10-slim-bullseye

RUN mkdir /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip install -r /usr/src/app/requirements.txt

RUN rm -r /usr/src/app