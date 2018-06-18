from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_restful_swagger import swagger


myApp = Flask(__name__)

myApp.config.from_pyfile('config.cfg')

myDb = SQLAlchemy(myApp)

myApi = Api(myApp)

# Если дебаг режим, подключаем сваггер доку, потыкаться можно по адресу http://127.0.0.1:5000/api/spec.html#!/spec
if myApp.debug:
    myApi = swagger.docs(Api(myApp), description="Description serials API", apiVersion='0.1.0')

myMa = Marshmallow(myApp)
