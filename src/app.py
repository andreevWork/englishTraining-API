from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_env import MetaFlaskEnv
import os


class Configuration(metaclass=MetaFlaskEnv):
    ENV = 'development'
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/postgres'

    SESSION_TYPE = 'filesystem'

    BASIC_AUTH_USERNAME = os.environ.get('BASIC_AUTH_USERNAME') or "admin"
    BASIC_AUTH_PASSWORD = os.environ.get('BASIC_AUTH_PASSWORD') or "admin"


myApp = Flask(__name__)

myApp.config.from_object(Configuration)
myApp.secret_key = os.environ.get('SECRET_KEY') or '12345'

CORS(myApp, origins=['http://localhost(:\d+)?', 'http://127.0.0.1(:\d+)?'])

myDb = SQLAlchemy(myApp)
myApi = Api(myApp)
myMa = Marshmallow(myApp)
