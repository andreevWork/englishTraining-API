from models.episodes import Episode, episode_schema
from models.serials import Serial, serial_schema

from flask_restful import Resource
from flask_restful_swagger import swagger
from sqlalchemy.orm import joinedload


@swagger.model
class EpisodesResource(Resource):
    @swagger.operation(
        notes='Getting all episodes all serials',
        responseClass=Episode.__name__,
    )
    def get(self):
        data = Episode.query\
            .join(Serial)

        for d in data:
            print(d, d.serial)

        return episode_schema.jsonify(data, many=True)
