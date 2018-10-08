from werkzeug.wrappers import Response
from werkzeug.utils import redirect
from werkzeug.exceptions import HTTPException

from src.app import myApi, myApp, myDb
from src.models.serials import Serial
from src.resourses.episodes import Episode
from flask_admin.contrib.sqla import ModelView
from flask_restful_swagger import swagger
from flask_admin import Admin
from flask_basicauth import BasicAuth

myBasicAuth = BasicAuth(myApp)


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


myAdmin = Admin(myApp, name='english-db')

myAdmin.add_view(MyModelView(Serial, myDb.session))
myAdmin.add_view(MyModelView(Episode, myDb.session))

# - сваггер доку, потыкаться можно по адресу http://127.0.0.1:5000/api/spec.html
swagger.docs(myApi, description="Description serials API")
