from flask_restful import Resource, reqparse
from model.Colaborador_model import Colaborador_model

atributos = reqparse.RequestParser()
atributos.add_argument('nome', type=str, required=True, help="The field 'nome' must be informed")
atributos.add_argument('id_cargo', type=int, required=True, help="The field 'id_cargo' must be informed")

class Colaboradores(Resource):
    def get(self):
        return {'colaboradores': [colaborador.json() for colaborador in Colaborador_model.query.all()]}

    def post(self):
        dados = atributos.parse_args()
        colaborador = Colaborador_model(**dados)
        colaborador.save_colaborador()
        return colaborador.json()

class Colaborador(Resource):
    def get(self, nome):
        colaborador = Colaborador_model.find_colaborador(nome)
        return colaborador.json()

    def delete(self, nome):
        colaborador = Colaborador_model.find_colaborador(nome)
        colaborador.delete_colaborador()
        return {'message': 'Colaborador deletado.'}