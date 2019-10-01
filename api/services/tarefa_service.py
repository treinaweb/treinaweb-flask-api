from ..models import tarefa_model
from api import db

def cadastrar_tarefa(tarefa):
    tarefa_bd = tarefa_model.Tarefa(titulo=tarefa.titulo, descricao=tarefa.descricao,
                                    data_expiracao=tarefa.data_expiracao)
    db.session.add(tarefa_bd)
    db.session.commit()
    return tarefa_bd