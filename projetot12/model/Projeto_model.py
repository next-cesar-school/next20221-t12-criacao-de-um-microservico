from sql_alchemy import db
from model.colaborador_model import Colaborador_model

projeto_colaborador = db.Table('projeto_colaborador',
                               db.Column('id_projeto', db.Integer, db.ForeignKey('projetos.id_projeto'), primary_key=True),
                               db.Column('id_colaborador', db.Integer, db.ForeignKey('colaboradores.id_colaborador'), primary_key=True))

class Projeto_model(db.Model):
    # id_colaborador = gerente
    __tablename__ = "projetos"
    id_projeto = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50))
    flag = db.Column(db.String(50))
    #data_inicio = db.Column(db.Date)
    #data_final = db.Column(db.Date)
    id_centro = db.Column(db.Integer, db.ForeignKey("centros.id_centro"))
    colaboradores = db.relationship('Colaborador_model', secondary=projeto_colaborador)


    def __init__(self, nome, status, flag, id_centro, colaboradores):
        self.nome = nome
        self.status = status
        self.flag = flag
        #self.data_inicio = data_inicio
        #self.data_final = data_final
        self.id_centro = id_centro
        #colaboradoresparser = [Colaborador_model(colaborador['nome'], colaborador['id_cargo'], colaborador['id_colaborador']) for colaborador  in colaboradores]
        self.colaboradores = [(Colaborador_model.find_by_id(colaborador['id_colaborador'])) for colaborador in colaboradores]

    def json(self):
        return {
            'id_projeto': self.id_projeto,
            'nome': self.nome,
            'status': self.status,
            'flag': self.flag,
            #'data_inicio': self.data_inicio,
            #'data_final': self.data_final,
            'id_centro': self.id_centro,
            'colaboradores': [colaborador.json() for colaborador in self.colaboradores]
        }

    def save_projeto(self):
        db.session.add(self)
        db.session.commit()

    def delete_projeto(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_projeto(cls, nome):
        projeto = cls.query.filter_by(nome=nome).first()
        if projeto:
            return projeto
        return None

    @classmethod
    def find_by_id(cls, id_projeto):
        projeto = cls.query.filter_by(id_projeto=id_projeto).first()
        if projeto:
            return projeto
        return None

    def update_projeto(self, nome, status, flag, id_centro, colaboradores):
        self.nome = nome
        self.status = status
        self.flag = flag
        #self.data_inicio = data_inicio
        #self.data_final = data_final
        self.id_centro = id_centro
        self.colaboradores = [(Colaborador_model.find_by_id(colaborador['id_colaborador'])) for colaborador in colaboradores]
