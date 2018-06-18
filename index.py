from app import myApi, myApp, myDb
from models.serials import Serial
from resourses.serials import SerialsResource, EpisodeResource

# myDb.session.add(Serial(season=1, episode=2, title='Test morty', videoSrc='qrqewrew', subtitleSrc='qfrqewfqre'))
# myDb.session.commit()

myApi.add_resource(SerialsResource, '/serials')
myApi.add_resource(EpisodeResource, '/serials/<int:episode_id>')


def start_server():
    myApp.run()


if __name__ == '__main__':
    start_server()
