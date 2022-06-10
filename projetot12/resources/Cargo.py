from flask_restful import Resource, reqparse
from model.Cargo_model import Cargo_model

atributos = reqparse.RequestParser()
atributos.add_argument('nome', type=str, required=True, help="The field 'nome' must be informed")

class Cargos(Resource):
    def get(self):
        return {'cargos': [cargo.json() for cargo in Cargo_model.query.all()]}

    def post(self):
        dados = atributos.parse_args()
        cargo = Cargo_model(**dados)
        cargo.save_cargo()
        return cargo.json()

class Cargo(Resource):
    def get(self, nome):
        return Cargo_model.find_cargo(nome)

    def delete(self, nome):
        cargo = Cargo_model.find_cargo(nome)
        cargo.delete_cargo()
        return {'message': 'Cargo deletado.'}