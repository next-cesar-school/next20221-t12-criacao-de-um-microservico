from SQL_Alchemy import db


class Centro_de_custo(db.Model):
    __tablename__ = "centros"
    id_centro = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, notnullable=True)

    def __init__(self, id_centro, nome):
        self.id_centro = id_centro
        self.nome = nome
