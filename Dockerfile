FROM python:3.6

ARG SQLALCHEMY_DATABASE_URI
ARG ENV='production'
ARG TESTING=False
ARG DEBUG=False

RUN apt-get update

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV SQLALCHEMY_DATABASE_URI=$SQLALCHEMY_DATABASE_URI
ENV ENV=$ENV
ENV TESTING=$TESTING
ENV DEBUG=$DEBUG

EXPOSE 5000

ENTRYPOINT ["python", "manage.py","start"]
