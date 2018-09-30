FROM python:3.6-alpine

LABEL maintainer "Eric Gu <eric.changning.gu@gmail.com>"

RUN apk update \
  && apk add \
    build-base \
    postgresql \
    postgresql-dev \
    libpq

RUN mkdir -p /srv/python

WORKDIR /srv/python

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["/srv/python/entrypoint.sh"]
