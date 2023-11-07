FROM python:3.11-slim-buster

WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /src

RUN pip install --upgrade pip && pip install -r /src/reqrequirements/base.txt