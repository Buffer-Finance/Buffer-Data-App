# Creating image based on official python3 image
FROM python:3.7.0
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir -p $APP_HOME
RUN mkdir -p $APP_HOME/staticfiles
WORKDIR $APP_HOME

# WORKDIR /
RUN apt-get update && apt-get install -f -y postgresql-client

# Installing all python dependencies
COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py ./

RUN ls