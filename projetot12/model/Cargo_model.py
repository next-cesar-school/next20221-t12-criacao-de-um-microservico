from SQL_Alchemy import db


class Cargo_model(db.Model):
    __tablename__ = "cargos"
    id_cargo = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))

    def __init__(self, id_cargo, nome):
        self.id_cargo = id_cargo
        self.nome = nome
