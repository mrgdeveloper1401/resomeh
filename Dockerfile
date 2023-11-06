FROM python:3.10-alpine

WORKDIR /src

COPY . /src
COPY /requirements/base.txt  /src/

RUN pip install -U pip
RUN pip install -r base.txt

EXPOSE 8000

CMD [ "gunicorn", "cv.wsgi", ":8000" ]