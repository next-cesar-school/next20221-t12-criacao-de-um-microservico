from flask_restful import Resource, reqparse
from model.colaborador_model import Colaborador_model
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from werkzeug.security import safe_str_cmp
from blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('matricula', type=int, required=True, help="O campo 'matricula' precisa ser informado")
atributos.add_argument('nome', type=str, required=True, help="O campo 'nome' precisa ser informado")
atributos.add_argument('id_cargo', type=int, required=True, help="O campo 'id_cargo' precisa ser informado")
atributos.add_argument('id_centro', type=int, required=True, help="O campo 'id_centro' precisa ser informado")
atributos.add_argument('login', type=str)
atributos.add_argument('senha', type=str)


class Colaboradores(Resource):
    def get(self):
        return {'colaboradores': [colaborador.json() for colaborador in Colaborador_model.query.all()]}

    
    def post(self):
        dados = atributos.parse_args()
        if Colaborador_model.find_by_login(dados['login']):
            return {"message": "O login '{}' já existe.".format(dados['login'])}
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
        colaborador = Colaborador_model.find_by_id(id_colaborador)
        if colaborador:
            return colaborador.json()
        return {'message': 'Colaborador não cadastrado.'}, 404

    @jwt_required()
    def put(self, id_colaborador):
        dados = atributos.parse_args()
        if Colaborador_model.find_by_login(dados['login']):
            return {"message": "O login '{}' já existe.".format(dados['login'])}
        colaborador_encontrado = Colaborador_model.find_by_id(id_colaborador)
        if colaborador_encontrado:
            colaborador_encontrado.update_colaborador(**dados)
            try:
                colaborador_encontrado.save_colaborador()
                return colaborador_encontrado.json(), 200
            except:
                return {"message": "Ocorreu um erro ao tentar atualizar o colaborador."}, 500 #internal server error
        return {'message': 'Colaborador não encontrado.'}, 404

    @jwt_required()
    def delete(self, id_colaborador):
        colaborador = Colaborador_model.find_colaborador(id_colaborador)
        if colaborador:
            colaborador.delete_colaborador()
            return {'message': 'Colaborador deletado.'}
        return {'message': 'Colaborador não encontrado.'}, 404

class Login(Resource):

    dados = reqparse.RequestParser()
    dados.add_argument('login', type=str, required=True, help="O campo 'login' deve ser informado")
    dados.add_argument('senha', type=str, required=True, help="O campo 'senha' deve ser informado")
    
    @classmethod
    def post(cls):
        auth = Login.dados.parse_args()
        colaborador = Colaborador_model.find_by_login(auth['login'])

        if colaborador and safe_str_cmp(colaborador.senha, auth['senha']):
            token_de_acesso = create_access_token(identity=colaborador.id_colaborador)
            return {'access_token': token_de_acesso}, 200
        return {'message': 'Login ou senha incorretos'}, 401  # unauthorized

class Logout(Resource):

    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti'] # JWT Token Identifier
        BLACKLIST.add(jwt_id)
        return {'message': 'Você saiu do sistema!'}, 200