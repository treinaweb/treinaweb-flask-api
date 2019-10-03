from api import db
from ..models import projeto_model

class Tarefa(db.Model):
    __tablename__ = "tarefa"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    titulo = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    data_expiracao = db.Column(db.Date, nullable=False)

    projeto_id = db.Column(db.Integer, db.ForeignKey("projeto.id"))
    projeto = db.relationship(projeto_model.Projeto, backref=db.backref("tarefas", lazy="dynamic"))