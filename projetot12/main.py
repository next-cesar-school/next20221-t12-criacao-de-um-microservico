from flask import Flask, jsonify
from flask_restful import Api
from resources.cargo import Cargos, Cargo
from resources.centro_de_custo import Centros_de_custo, Centro_de_custo
from resources.colaborador import Colaboradores, Colaborador, Login, Logout
from resources.projeto import Projetos, Projeto
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:$yz8tq,os2zm*#@localhost/dbpython'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
app.config['JWT_BLACKLIST_ENABLED'] = True
api = Api(app)
jwt = JWTManager(app)


@app.before_first_request
def criar_banco():
    db.create_all()


@jwt.token_in_blocklist_loader
def verifica_blacklist(self, token):
    return token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def token_de_acesso_invalidado(jwt_header, jwt_payload):
    return jsonify({'message': 'Você não está autenticado no sistema.'}), 401 # unauthorized


@app.route('/')
def pag_inicial():
    return '<h1>REST API com Flask para gestão de projetos!!</h1>'


api.add_resource(Cargos, '/cargos')
api.add_resource(Cargo, '/cargos/<string:nome>')
api.add_resource(Centros_de_custo, '/centros')
api.add_resource(Centro_de_custo, '/centros/<string:nome>')
api.add_resource(Colaboradores, '/colaboradores')
api.add_resource(Colaborador, '/colaboradores/<int:id_colaborador>')
api.add_resource(Projetos, '/projetos')
api.add_resource(Projeto, '/projetos/<int:id_projeto>')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')

if __name__ == "__main__":
    from sql_alchemy import db
    db.init_app(app)
    app.run(debug=True)
