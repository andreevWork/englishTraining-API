from app import myApi, myApp, myDb
from resourses.episodes import EpisodesResource

myApi.add_resource(EpisodesResource, '/episodes')


def start_server():
    myApp.run()


if __name__ == '__main__':
    myDb.create_all()
    start_server()
