from flask_restful import Resource, reqparse
from model.centro_de_custo_model import Centro_de_custo_model

atributos = reqparse.RequestParser()
atributos.add_argument('nome', type=str, required=True, help="The field 'nome' must be informed")

class Centros_de_custo(Resource):
    def get(self):
        return {'centros': [centro.json() for centro in Centro_de_custo_model.query.all()]}

    def post(self):
        dados = atributos.parse_args()
        centro = Centro_de_custo_model(**dados)
        isCentro = Centro_de_custo_model.find_centro(centro.nome)
        if isCentro:
            return {'message': "O centro de custo '{} já está cadastrado.".format(centro.nome)}, 400
        try:
            centro.save_centro()
        except:
            return {"message": "Ocorreu um erro ao tentar cadastrar o novo centro de custo."}, 500 #internal server error
        return centro.json(), 201

class Centro_de_custo(Resource):
    def get(self, nome):
        centro = Centro_de_custo_model.find_centro(nome)
        if centro:
            return centro.json()
        return {'message': 'Centro não cadastrado.'}, 404

    def delete(self, nome):
        centro = Centro_de_custo_model.find_centro(nome)
        if centro:
            centro.delete_centro()
            return {'message': 'Centro deletado.'}
        return {'message': 'Centro não cadastrado.'}, 404