from ..models import projeto_model
from api import db
from ..services.funcionario_service import listar_funcionario_id

def cadastrar_projeto(projeto):
    projeto_bd = projeto_model.Projeto(nome=projeto.nome, descricao=projeto.descricao)
    for i in projeto.funcionarios:
        funcionario = listar_funcionario_id(i)
        projeto_bd.funcionarios.append(funcionario)
    db.session.add(projeto_bd)
    db.session.commit()
    return projeto_bd

def listar_projetos():
    projetos = projeto_model.Projeto.query.all()
    return projetos

def listar_projeto_id(id):
    projeto = projeto_model.Projeto.query.filter_by(id=id).first()
    return projeto

def editar_projeto(projeto_bd, projeto_novo):
    projeto_bd.nome = projeto_novo.nome
    projeto_bd.descricao = projeto_novo.descricao
    projeto_bd.funcionarios = []
    for i in projeto_novo.funcionarios:
        funcionario = listar_funcionario_id(i)
        projeto_bd.funcionarios.append(funcionario)
    db.session.commit()

def remover_projeto(projeto):
    db.session.delete(projeto)
    db.session.commit()