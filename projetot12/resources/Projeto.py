from flask_restful import Resource, reqparse
from model.Projeto_model import Projeto_model

atributos = reqparse.RequestParser()
atributos.add_argument('nome', type=str, required=True, help="The field 'nome' must be informed")
atributos.add_argument('status', type=str)
atributos.add_argument('flag', type=str)
atributos.add_argument('id_centro', type=int, required=True, help="The field 'id_centro' must be informed")
atributos.add_argument('colaboradores', type=int, required=True, help="The field 'colaboradores' must be informed")

#nome, status, flag, id_centro
class Projetos(Resource):
    def get(self):
        return {'projetos': [projeto.json() for projeto in Projeto_model.query.all()]}

    def post(self):
        dados = atributos.parse_args()
        projeto = Projeto_model(**dados)
        projeto.save_projeto()
        return projeto.json()

class Projeto(Resource):
    def get(self, nome):
        projeto = Projeto_model.find_projeto(nome)
        return projeto.json()

    def put(self, nome):
      pass

    def delete(self, nome):
        projeto = Projeto_model.find_projeto(nome)
        projeto.delete_projeto()
        return {'message': 'Projeto apagado.'}