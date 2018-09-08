from werkzeug.wrappers import Response
from werkzeug.utils import redirect
from werkzeug.exceptions import HTTPException

from app import myApi, myApp, myDb
from flask_restful import Api
from models.serials import Serial
from resourses.episodes import EpisodesResource, Episode
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_restful_swagger import swagger
from flask_admin import Admin
from flask_basicauth import BasicAuth
import os


myApi.add_resource(EpisodesResource, '/episodes')

# - сваггер доку, потыкаться можно по адресу http://127.0.0.1:5000/api/spec.html#!/spec
# - админку для зависимостей
myApp.config['BASIC_AUTH_USERNAME'] = os.environ.get('BASIC_AUTH_USERNAME') or "admin"
myApp.config['BASIC_AUTH_PASSWORD'] = os.environ.get('BASIC_AUTH_PASSWORD') or "12345"

myBasicAuth = BasicAuth(myApp)

myApi = swagger.docs(Api(myApp), description="Description serials API", apiVersion='0.1.0')


class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(message, Response(
            "You could not be authenticated. Please refresh the page.", 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        ))


class MyModelView(ModelView):
    def is_accessible(self):
        if not myBasicAuth.authenticate():
            raise AuthException('Not authenticated.')
        else:
            return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(myBasicAuth.challenge())


# Чтобы работала сессия базы на запись
myApp.secret_key = os.environ.get('SECRET_KEY') or '234'
myApp.config['SESSION_TYPE'] = 'filesystem'

myAdmin = Admin(myApp, name='english-db')

myAdmin.add_view(MyModelView(Serial, myDb.session))
myAdmin.add_view(MyModelView(Episode, myDb.session))

myAdmin.add_view(FileAdmin('./static', name='Static Files'))

def start_server():
    myApp.run(host='0.0.0.0')


if __name__ == '__main__':
    myDb.create_all()
    start_server()
