from flask_restful import Resource, reqparse
from model.colaborador_model import Colaborador_model

atributos = reqparse.RequestParser()
atributos.add_argument('matricula', type=int, required=True, help="O campo 'matricula' precisa ser informado")
atributos.add_argument('nome', type=str, required=True, help="O campo 'nome' precisa ser informado")
atributos.add_argument('id_cargo', type=int, required=True, help="O campo 'id_cargo' precisa ser informado")
atributos.add_argument('id_centro', type=int, required=True, help="O campo 'id_centro' precisa ser informado")


class Colaboradores(Resource):
    def get(self):
        return {'colaboradores': [colaborador.json() for colaborador in Colaborador_model.query.all()]}

    def post(self):
        dados = atributos.parse_args()
        colaborador = Colaborador_model(**dados)
        isColaborador = Colaborador_model.find_colaborador(colaborador.matricula)
        if isColaborador:
            return {'message': "O colaborador '{} já está cadastrado.".format(colaborador.matricula)}, 400
        try:
            colaborador.save_colaborador()
        except:
            return {"message": "Ocorreu um erro ao tentar cadastrar o novo colaborador."}, 500 #internal server error
        return colaborador.json(), 201

class Colaborador(Resource):
    def get(self, id_colaborador):
        colaborador = Colaborador_model.find_colaborador(id_colaborador)
        if colaborador:
            return colaborador.json()
        return {'message': 'Colaborador não cadastrado.'}, 404

    def put(self, id_colaborador):
        dados = atributos.parse_args()
        colaborador_encontrado = Colaborador_model.find_by_id(id_colaborador)
        if colaborador_encontrado:
            colaborador_encontrado.update_colaborador(**dados)
            try:
                colaborador_encontrado.save_colaborador()
                return colaborador_encontrado.json(), 200
            except:
                return {"message": "Ocorreu um erro ao tentar atualizar o colaborador."}, 500 #internal server error
        return {'message': 'Colaborador não encontrado.'}, 404

    def delete(self, id_colaborador):
        colaborador = Colaborador_model.find_colaborador(id_colaborador)
        if colaborador:
            colaborador.delete_colaborador()
            return {'message': 'Colaborador deletado.'}
        return {'message': 'Colaborador não encontrado.'}, 404