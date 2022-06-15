from sql_alchemy import db


class Colaborador_model(db.Model):
    __tablename__ = "colaboradores"
    id_colaborador = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.Integer, nullable=False, unique=True)
    nome = db.Column(db.String(100), nullable=False)
    id_cargo = db.Column(db.Integer, db.ForeignKey("cargos.id_cargo"))
    id_centro = db.Column(db.Integer, db.ForeignKey("centros.id_centro"))
    login = db.Column(db.String(50))
    senha = db.Column(db.String(50))

    def __init__(self, matricula, nome, id_cargo, id_centro, login, senha):
        self.matricula = matricula
        self.nome = nome
        self.id_cargo = id_cargo
        self.id_centro = id_centro
        self.login = login
        self.senha = senha

    def json(self):
        return {
            'id_colaborador': self.id_colaborador,
            'matricula': self.matricula,
            'nome': self.nome,
            'id_cargo': self.id_cargo,
            'id_centro': self.id_centro,
            'login': self.login
        }

    def save_colaborador(self):
        db.session.add(self)
        db.session.commit()

    def delete_colaborador(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_colaborador(cls, matricula):
        colaborador = cls.query.filter_by(matricula=matricula).first()
        if colaborador:
            return colaborador
        return None

    @classmethod
    def find_by_id(cls, id_colaborador):
        colaborador = cls.query.filter_by(id_colaborador=id_colaborador).first()
        if colaborador:
            return colaborador
        return None

    @classmethod
    def find_by_login(cls, login):
        # SELECT * FROM usuarios WHERE login = $login
        colaborador = cls.query.filter_by(login=login).first()
        if colaborador:
            return colaborador
        return None

    def update_colaborador(self, nome, id_cargo, id_centro, login, senha):
        self.nome = nome
        self.id_cargo = id_cargo
        self.id_centro = id_centro
        self.login = login
        self.senha = senha