from flask_restful import Resource, reqparse
from model.Centro_de_custo_model import Centro_de_custo_model

atributos = reqparse.RequestParser()
atributos.add_argument('nome', type=str, required=True, help="The field 'nome' must be informed")

class Centros_de_custo(Resource):
    def get(self):
        return {'centros': [centro.json() for centro in Centro_de_custo_model.query.all()]}

    def post(self):
        dados = atributos.parse_args()
        centro = Centro_de_custo_model(**dados)
        centro.save_centro()
        return centro.json()

class Centro_de_custo(Resource):
    def get(self, nome):
        centro = Centro_de_custo_model.find_centro(nome)
        return centro.json()

    def delete(self, nome):
        centro = Centro_de_custo_model.find_centro(nome)
        centro.delete_centro()
        return {'message': 'Centro deletado.'}