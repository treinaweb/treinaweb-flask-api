from api import db

class Funcionario(db.Model):
    __tablename__ = "funcionario"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.Integer, nullable=False)

    projetos = db.relationship("Projeto", secondary="funcionario_projeto", back_populates="funcionarios")