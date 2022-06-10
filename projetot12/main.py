from flask import Flask
from flask_restful import Api
from resources.Cargo import Cargos, Cargo
from resources.Centro_de_custo import Centros_de_custo, Centro_de_custo
from resources.Colaborador import Colaboradores, Colaborador
from resources.Projeto import Projetos, Projeto


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:$yz8tq,os2zm*#@localhost/dbpython'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def criar_banco():
    db.create_all()

@app.route('/')
def pag_inicial():
    return '<h1>API Projetos!!</h1>'

api.add_resource(Cargos, "/cargos")
api.add_resource(Cargo, "/cargos/<string:nome>")
api.add_resource(Centros_de_custo, "/centros")
api.add_resource(Centro_de_custo, "/centros/<string:nome>")
api.add_resource(Colaboradores, '/colaboradores')
api.add_resource(Colaborador, '/colaboradores/<string:nome>')
api.add_resource(Projetos, '/projetos')
api.add_resource(Projeto, '/projetos/<string:nome>')

if __name__ == "__main__":
    from sql_alchemy import db
    db.init_app(app)
    app.run(debug=True)

