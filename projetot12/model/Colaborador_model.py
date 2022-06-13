from sql_alchemy import db


class Colaborador_model(db.Model):
    __tablename__ = "colaboradores"
    id_colaborador = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    id_cargo = db.Column(db.Integer, db.ForeignKey("cargos.id_cargo"))

    def __init__(self, nome, id_cargo, id_colaborador=None):
        if id_colaborador != None:
            self.id_colaborador = id_colaborador
        self.nome = nome
        self.id_cargo = id_cargo

    def json(self):
        return {
            'id_colaborador': self.id_colaborador,
            'nome': self.nome,
            'id_cargo': self.id_cargo
        }

    def save_colaborador(self):
        db.session.add(self)
        db.session.commit()

    def delete_colaborador(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_colaborador(cls, nome):
        colaborador = cls.query.filter_by(nome=nome).first()
        if colaborador:
            return colaborador
        return None