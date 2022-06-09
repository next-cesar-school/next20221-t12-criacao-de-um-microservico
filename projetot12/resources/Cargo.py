from flask_restful import Resource
from model.Cargo_model import Cargo_model

class Cargos(Resource):
    def get(self):
        return {"cargos": [cargo for cargo in Cargo_model.query.all()]} 