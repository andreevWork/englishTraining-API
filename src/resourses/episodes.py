from src.models.episodes import Episode, episode_schema

from flask_restful import Resource
from flask_restful_swagger import swagger

from src.models.serials import Serial


@swagger.model
class EpisodesResource(Resource):
    @swagger.operation(
        notes='Getting all episodes all serials',
        responseClass=Episode.__name__,
    )
    def get(self, serial_id):
        data = Episode.query.join(Serial).filter(Serial.id == serial_id)

        return episode_schema.jsonify(data, many=True)
