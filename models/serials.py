from app import myDb, myMa


class Serial(myDb.Model):
    id = myDb.Column(myDb.Integer, primary_key=True)
    season = myDb.Column(myDb.Integer, nullable=False)
    episode = myDb.Column(myDb.Integer, nullable=False)
    title = myDb.Column(myDb.String(120), nullable=False)
    videoSrc = myDb.Column(myDb.String(120), nullable=False)
    subtitleSrc = myDb.Column(myDb.String(120), nullable=False)


class SerialSchema(myMa.ModelSchema):
    class Meta:
        model = Serial


serial_schema = SerialSchema()
