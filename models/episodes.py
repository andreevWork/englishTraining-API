from app import myDb, myMa
from models.serials import SerialSchema, Serial


class Episode(myDb.Model):
    id = myDb.Column(myDb.Integer, primary_key=True)

    serial_id = myDb.Column(myDb.Integer, myDb.ForeignKey('serial.id'), nullable=False)
    serial = myDb.relationship('Serial')

    season = myDb.Column(myDb.Integer, nullable=False)
    episode = myDb.Column(myDb.Integer, nullable=False)
    title = myDb.Column(myDb.String(120), nullable=False)
    videoSrc = myDb.Column(myDb.String(120), nullable=False)
    previewImageSrc = myDb.Column(myDb.String(120))
    subtitleSrc = myDb.Column(myDb.String(120), nullable=False)


class EpisodeSchema(myMa.ModelSchema):
    class Meta:
        model = Episode

    serial = myMa.Nested(SerialSchema)


episode_schema = EpisodeSchema()
