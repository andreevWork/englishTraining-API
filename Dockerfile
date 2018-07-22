FROM python:3.6

RUN apt-get update

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV SQLALCHEMY_DATABASE_URI
ENV ENV production
ENV TESTING False
ENV DEBUG False

EXPOSE 5000

ENTRYPOINT ["python", "manage.py","start"]
