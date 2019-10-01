from ..models import tarefa_model
from api import db

def cadastrar_tarefa(tarefa):
    tarefa_bd = tarefa_model.Tarefa(titulo=tarefa.titulo, descricao=tarefa.descricao,
                                    data_expiracao=tarefa.data_expiracao)
    db.session.add(tarefa_bd)
    db.session.commit()
    return tarefa_bd

def listar_tarefas():
    tarefas = tarefa_model.Tarefa.query.all()
    return tarefas

def listar_tarefa_id(id):
    tarefa = tarefa_model.Tarefa.query.filter_by(id=id).first()
    return tarefa

def editar_tarefa(tarefa_bd, tarefa_nova):
    tarefa_bd.titulo = tarefa_nova.titulo
    tarefa_bd.descricao = tarefa_nova.descricao
    tarefa_bd.data_expiracao = tarefa_nova.data_expiracao
    db.session.commit()

def remover_tarefa(tarefa):
    db.session.delete(tarefa)
    db.session.commit()