from app import myApi, myApp, myDb
from resourses.episodes import EpisodesResource

myApi.add_resource(EpisodesResource, '/episodes')


def start_server():
    myApp.run(host='0.0.0.0')


if __name__ == '__main__':
    myDb.create_all()
    start_server()
