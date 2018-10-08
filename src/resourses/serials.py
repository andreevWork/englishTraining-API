from sqlalchemy import asc

from flask_restful import Resource
from flask_restful_swagger import swagger

from src.models.serials import Serial


@swagger.model
class SerialsResource(Resource):
    @swagger.operation(
        notes='Getting all serials',
        responseClass=Serial.__name__,
    )
    def get(self):
        data = Serial.query.order_by(asc(Serial.id)).all()

        return serial_schema.jsonify(data, many=True)
