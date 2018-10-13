from src.app import myDb, myMa
from src.models.serials import SerialSchema


class Episode(myDb.Model):
    id = myDb.Column(myDb.Integer, primary_key=True)

    serial_id = myDb.Column(myDb.Integer, myDb.ForeignKey('serial.id'), nullable=False)
    serial = myDb.relationship('Serial')

    season = myDb.Column(myDb.Integer, nullable=False)
    episode = myDb.Column(myDb.Integer, nullable=False)
    title = myDb.Column(myDb.String(120), nullable=False)


class EpisodeSchema(myMa.ModelSchema):
    class Meta:
        model = Episode

    serial = myMa.Nested(SerialSchema)


episode_schema = EpisodeSchema()
