from SQL_Alchemy import db


class Projeto_model(db.Model):
    # id_colaborador = gerente
    __tablename__ = "projetos"
    id_projeto = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Integer(50))
    status = db.Column(db.String)
    flag = db.Column(db.String)
    id_centro = db.Column(db.Integer, db.ForeignKey("centros.id_centro"))

    def __init__(self, id_projeto, nome, status, flag, id_colaborador, id_centro):
        self.id_projeto = id_projeto
        self.nome = nome
        self.status = status
        self.flag = flag
        self.id_colaborador = id_colaborador
        self.id_centro = id_centro
