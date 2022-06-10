from sql_alchemy import db

projeto_colaborador = db.Table("projeto_colaborador",
                               db.Column(db.Integer, db.ForeignKey("colaboradores.id_colaborador")),
                               db.Column(db.Integer, db.ForeignKey("projetos.id_projeto")))


class Colaborador_model(db.Model):
    __tablename__ = "colaboradores"
    id_colaborador = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    id_cargo = db.Column(db.Integer, db.ForeignKey("cargos.id_cargo"))

    def __init__(self, nome, id_cargo):
        self.nome = nome
        self.id_cargo = id_cargo

