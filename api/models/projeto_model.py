from api import db
from .funcionario_model import Funcionario

funcionario_projeto = db.Table('funcionario_projeto',
               db.Column('projeto_id', db.Integer, db.ForeignKey('projeto.id'), primary_key=True, nullable=False),
               db.Column('funcionario_id', db.Integer, db.ForeignKey('funcionario.id'), primary_key=True, nullable=False)
                               )


class Projeto(db.Model):
    __tablename__ = "projeto"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)

    funcionarios = db.relationship(Funcionario, secondary="funcionario_projeto", back_populates="projetos")