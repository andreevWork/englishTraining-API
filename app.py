from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_marshmallow import Marshmallow
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

myMa = Marshmallow(myApp)
