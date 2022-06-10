from sql_alchemy import db

class Cargo_model(db.Model):
    __tablename__ = "cargos"
    id_cargo = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    colaboradores = db.relationship('Colaborador_model')

    def __init__(self, nome):
        self.nome = nome

    def json(self):
        return {
            'id_cargo': self.id_cargo,
            'nome': self.nome,
            'colaboradores': [colaborador.json() for colaborador in self.colaboradores]
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