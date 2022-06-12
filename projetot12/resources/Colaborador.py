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
        isColaborador = Colaborador_model.find_colaborador(colaborador.nome)
        if isColaborador:
            return {'message': "O colaborador '{} já está cadastrado.".format(colaborador.nome)}, 400
        try:
            colaborador.save_colaborador()
        except:
            return {"message": "Ocorreu um erro ao tentar cadastrar o novo colaborador."}, 500 #internal server error
        return colaborador.json(), 201

class Colaborador(Resource):
    def get(self, nome):
        colaborador = Colaborador_model.find_colaborador(nome)
        if colaborador:
            return colaborador.json()
        return {'message': 'Colaborador não cadastrado.'}, 404

    def delete(self, nome):
        colaborador = Colaborador_model.find_colaborador(nome)
        if colaborador:
            colaborador.delete_colaborador()
            return {'message': 'Colaborador deletado.'}
        return {'message': 'Colaborador não encontrado.'}, 404