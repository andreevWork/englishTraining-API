from src.app import myDb, myMa


class Serial(myDb.Model):
    id = myDb.Column(myDb.Integer, primary_key=True)
    title = myDb.Column(myDb.String(120), nullable=False)
    static_dirname = myDb.Column(myDb.String(120))
    description = myDb.Column(myDb.Text())


class SerialSchema(myMa.ModelSchema):
    class Meta:
        model = Serial


serial_schema = SerialSchema()
