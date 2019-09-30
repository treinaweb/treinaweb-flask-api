from flask_restful import Resource
from api import api

class TarefaList(Resource):
    def get(self):
        return "Olá mundo"

api.add_resource(TarefaList, '/tarefas')