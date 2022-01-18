FROM python:3.7-alpine3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING utf-8

COPY ./requirements.txt /
WORKDIR /code

# install packages
RUN    apk add --no-cache mariadb-dev mariadb-connector-c-dev \
    && apk add --no-cache --virtual .build-deps gcc g++ libgcc libstdc++ libc-dev linux-headers shadow \
    && pip install --upgrade pip \
    && pip install -r /requirements.txt \
    && useradd -s /sbin/nologin -M -d /dev/null uwsgi \
    && apk del .build-deps \
    && rm -rf /root/.cache /var/cache/apk/* /tmp/*

EXPOSE 8081

CMD ["uwsgi", "--ini", "/uwsgi.ini"]
