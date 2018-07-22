from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_restful_swagger import swagger
from flask_cors import CORS
from flask_env import MetaFlaskEnv


class Configuration(metaclass=MetaFlaskEnv):
    ENV = 'development'
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/postgres'


myApp = Flask(__name__)

myApp.config.from_object(Configuration)

CORS(myApp)

myDb = SQLAlchemy(myApp)

myApi = Api(myApp)

# Если дебаг режим, подключаем сваггер доку, потыкаться можно по адресу http://127.0.0.1:5000/api/spec.html#!/spec
if myApp.debug:
    myApi = swagger.docs(Api(myApp), description="Description serials API", apiVersion='0.1.0')

myMa = Marshmallow(myApp)
