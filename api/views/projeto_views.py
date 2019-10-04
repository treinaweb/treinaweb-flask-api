from flask_restful import Resource
from api import api
from ..schemas import projeto_schema
from flask import request, make_response, jsonify
from ..entidades import projeto
from ..services import projeto_service

class ProjetoList(Resource):
    def get(self):
        projetos = projeto_service.listar_projetos()
        ps = projeto_schema.ProjetoSchema(many=True)
        return make_response(ps.jsonify(projetos), 200)

    def post(self):
        ps = projeto_schema.ProjetoSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            funcionarios = request.json["funcionarios"]
            projeto_novo = projeto.Projeto(nome=nome, descricao=descricao, funcionarios=funcionarios)
            result = projeto_service.cadastrar_projeto(projeto_novo)
            return make_response(ps.jsonify(result), 201)

class ProjetoDetail(Resource):
    def get(self, id):
        projeto = projeto_service.listar_projeto_id(id)
        if projeto is None:
            return make_response(jsonify("Projeto não encontrado"), 404)
        ps = projeto_schema.ProjetoSchema()
        return make_response(ps.jsonify(projeto), 200)

    def put(self, id):
        projeto_bd = projeto_service.listar_projeto_id(id)
        if projeto_bd is None:
            return make_response(jsonify("Projeto não encontrado"), 404)
        ps = projeto_schema.ProjetoSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            funcionarios = request.json["funcionarios"]
            projeto_novo = projeto.Projeto(nome=nome, descricao=descricao, funcionarios=funcionarios)
            projeto_service.editar_projeto(projeto_bd, projeto_novo)
            projeto_atualizado = projeto_service.listar_projeto_id(id)
            return make_response(ps.jsonify(projeto_atualizado), 200)

    def delete(self, id):
        projeto = projeto_service.listar_projeto_id(id)
        if projeto is None:
            return make_response(jsonify("Projeto não encontrado"), 404)
        projeto_service.remover_projeto(projeto)
        return make_response('', 204)

api.add_resource(ProjetoList, '/projetos')
api.add_resource(ProjetoDetail, '/projetos/<int:id>')