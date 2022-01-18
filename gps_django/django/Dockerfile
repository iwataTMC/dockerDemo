FROM python:3.7-alpine3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING utf-8

COPY ./requirements.txt /
WORKDIR /code

# install packages
RUN    pip install --upgrade pip \
    && pip install -r /requirements.txt

EXPOSE 8780

CMD ["python", "manage.py", "runserver", "0.0.0.0:8780"]
