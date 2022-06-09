from flask import Flask
from flask_restful import Api


from resources.Cargo import Cargos

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
api = Api(app)

@app.before_first_request
def criar_banco():
    db.create_all()

api.add_resource(Cargos, "/cargos")

if __name__ == "__main__":
    from SQL_Alchemy import db
    db.init_app(app)
    app.run(debug=True)