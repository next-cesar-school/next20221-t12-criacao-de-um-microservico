from sql_alchemy import db

class Cargo_model(db.Model):
    __tablename__ = "cargos"
    id_cargo = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)

    def __init__(self, nome):
        self.nome = nome

    def json(self):
        return {
            'id_cargo': self.id_cargo,
            'nome': self.nome
        }

    def save_cargo(self):
        db.session.add(self)
        db.session.commit()

    def delete_cargo(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_cargo(cls, nome):
        cargo = cls.query.filter_by(nome=nome).first()
        return cargo