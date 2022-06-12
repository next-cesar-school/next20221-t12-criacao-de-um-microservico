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
        isProjeto = Projeto_model.find_projeto(projeto.nome)
        if isProjeto:
            return {'message': "O projeto '{} já está cadastrado.".format(projeto.nome)}, 400
        try:
            projeto.save_projeto()
        except:
            return {"message": "Ocorreu um erro ao tentar cadastrar o novo projeto."}, 500 #internal server error
        return projeto.json(), 201

class Projeto(Resource):
    def get(self, nome):
        projeto = Projeto_model.find_projeto(nome)
        if projeto:
            return projeto.json()
        return {'message': 'Projeto não cadastrado.'}, 404

    def delete(self, nome):
        projeto = Projeto_model.find_projeto(nome)
        if projeto:
            projeto.delete_projeto()
            return {'message': 'Projeto apagado.'}
        return {'message': 'Projeto não encontrado.'}, 404

class UpdateProjeto(Resource):
    def put(self, id_projeto):
        dados = atributos.parse_args()
        projeto_encontrado = Projeto_model.find_by_id(id_projeto)
        if projeto_encontrado:
            projeto_encontrado.update_projeto(**dados)
            try:
                projeto_encontrado.save_projeto()
                return projeto_encontrado.json(), 200
            except:
                return {"message": "Ocorreu um erro ao tentar atualizar o projeto."}, 500 #internal server error
        return {'message': 'Projeto não encontrado.'}, 404