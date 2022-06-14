from flask_restful import Resource, reqparse
from model.cargo_model import Cargo_model

atributos = reqparse.RequestParser()
atributos.add_argument('nome', type=str, required=True, help="The field 'nome' must be informed")

class Cargos(Resource):
    def get(self):
        return {'cargos': [cargo.json() for cargo in Cargo_model.query.all()]}

    def post(self):
        dados = atributos.parse_args()
        cargo = Cargo_model(**dados)
        isCargo = Cargo_model.find_cargo(cargo.nome)
        if isCargo:
            return {'message': "O cargo '{} já está cadastrado.".format(cargo.nome)}, 400
        try:
            cargo.save_cargo()
        except:
            return {"message": "Ocorreu um erro ao tentar cadastrar o novo cargo."}, 500 #internal server error
        return cargo.json(), 201

class Cargo(Resource):
    def get(self, nome):
        cargo = Cargo_model.find_cargo(nome)
        if cargo:
            return cargo.json()
        return {'message': 'Cargo não cadastrado.'}, 404

    def delete(self, nome):
        cargo = Cargo_model.find_cargo(nome)
        if cargo:
            cargo.delete_cargo()
            return {'message': 'Cargo apagado.'}
        return {'message': 'Cargo não encontrado.'}, 404