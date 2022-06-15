from flask_restful import Resource, reqparse
from model.projeto_model import Projeto_model


atributos = reqparse.RequestParser()
atributos.add_argument('nome', type=str, required=True, help="The field 'nome' must be informed")
atributos.add_argument('status', type=str)
atributos.add_argument('flag', type=str)
atributos.add_argument('data_inicio', type=str, location='json')
atributos.add_argument('data_final', type=str, location='json')
atributos.add_argument('id_centro', type=int, required=True, help="The field 'id_centro' must be informed")
atributos.add_argument('colaboradores', type=dict, action='append', location='json', required=True, help="The field 'colaboradores' must be informed")


class Projetos(Resource):
    def get(self):
        return {'projetos': [projeto.json() for projeto in Projeto_model.query.all()]}

    def post(self):
        dados = atributos.parse_args()
        projeto = Projeto_model(**dados)
        for i in projeto.colaboradores:
            if i.id_cargo == 1:
                isProjeto = Projeto_model.find_projeto(projeto.nome)
                if isProjeto:
                    return {'message': "O projeto '{} já está cadastrado.".format(projeto.nome)}, 400
                try:
                    projeto.save_projeto()
                except:
                    # internal server error
                    return {"message": "Ocorreu um erro ao tentar cadastrar o novo projeto."}, 500
                return projeto.json(), 201
        # bad request
        return {"message": "É necessário designar ao menos um gerente para o projeto."}, 400


class Projeto(Resource):
    def get(self, id_projeto):
        projeto = Projeto_model.find_by_id(id_projeto)
        if projeto:
            return projeto.json()
        return {'message': 'Projeto não cadastrado.'}, 404

    def put(self, id_projeto):
        dados = atributos.parse_args()
        projeto_encontrado = Projeto_model.find_by_id(id_projeto)
        if projeto_encontrado:
            projeto_encontrado.update_projeto(**dados)
            for i in projeto_encontrado.colaboradores:
                if i.id_cargo == 1:
                    try:
                        projeto_encontrado.save_projeto()
                        return projeto_encontrado.json(), 200
                    except:
                        # internal server error
                        return {"message": "Ocorreu um erro ao tentar atualizar o projeto."}, 500
            # bad request
            return {"message": "É necessário designar ao menos um gerente para o projeto."}, 400
        return {'message': 'Projeto não encontrado.'}, 404

    def delete(self, id_projeto):
        projeto = Projeto_model.find_by_id(id_projeto)
        if projeto:
            projeto.delete_projeto()
            return {'message': 'Projeto apagado.'}
        return {'message': 'Projeto não encontrado.'}, 404