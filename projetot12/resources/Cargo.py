from flask_restful import Resource
from model.Cargo_model import Cargo_model

class Cargos(Resource):
    def get(self):
        return {1:"Gerente", 2:"Desenvolvedor", 3:"Designer"}