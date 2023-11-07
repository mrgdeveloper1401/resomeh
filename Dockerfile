FROM python:3.11-slim-buster

WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /src
COPY ./requirements/base.txt /src/requirements/base.txt

RUN apt update && apt upgrade -y build-essential libpq-dev
RUN rm -rf /var/lib/lists/*

RUN pip install -r /src/requirements/base.txt