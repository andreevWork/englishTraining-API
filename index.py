from src.app import myApi, myApp, myDb
from src.resourses.episodes import EpisodesResource
from src.resourses.serials import SerialsResource
import src.admin

myApi.add_resource(EpisodesResource, '/episodes/<string:serial_id>')
myApi.add_resource(SerialsResource, '/serials')


def start_server():
    myApp.run(host='0.0.0.0')


if __name__ == '__main__':
    myDb.create_all()
    start_server()
