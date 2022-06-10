from sql_alchemy import db


class Centro_de_custo_model(db.Model):
    __tablename__ = "centros"
    id_centro = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)

    def __init__(self, nome):
        self.nome = nome

    def json(self):
        return {
            'id_centro': self.id_centro,
            'nome': self.nome
        }

    def save_centro(self):
        db.session.add(self)
        db.session.commit()

    def delete_centro(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_centro(cls, nome):
        centro = cls.query.filter_by(nome=nome).first()
        return centro