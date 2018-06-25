from models.serials import Serial, serial_schema
from flask_restful import Resource, abort
from flask_restful_swagger import swagger

# Решил пока не делать отдельные ручки, а все отдавать в общей коллекции
# @swagger.model
# class EpisodeResource(Resource):
#     @swagger.operation(
#         notes='Getting episode by id',
#         responseClass=Serial.__name__,
#         parameters=[
#             {
#                 "name": "episode_id",
#                 "dataType": "int",
#                 "paramType": "path"
#             }
#         ],
#         responseMessages=[
#             {
#                 "code": 404,
#                 "message": "Episode with such id doesn't exist"
#             }
#         ]
#     )
#     def get(self, episode_id):
#         data = Serial.query.filter_by(id=episode_id).first()
#
#         if not data:
#             abort(404, message="Episode with id={} doesn't exist".format(episode_id))
#
#         return serial_schema.jsonify(data)


@swagger.model
class SerialsResource(Resource):
    @swagger.operation(
        notes=
        'Getting all episodes all serials with less count of properties, only will get (id, episode, season, title)',
        responseClass=Serial.__name__,
    )
    def get(self):
        data = Serial.query.all()

        return serial_schema.jsonify(data, many=True)
