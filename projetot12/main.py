from flask import Flask
from flask_restful import Api
from resources.cargo import Cargos, Cargo
from resources.centro_de_custo import Centros_de_custo, Centro_de_custo
from resources.colaborador import Colaboradores, Colaborador
from resources.projeto import projetos, projeto, Update_projeto


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
api.add_resource(projetos, '/projetos')
api.add_resource(projeto, '/projetos/<string:nome>')
api.add_resource(Update_projeto, '/projetos/<string:id_projeto>')

if __name__ == "__main__":
    from sql_alchemy import db
    db.init_app(app)
    app.run(debug=True)

