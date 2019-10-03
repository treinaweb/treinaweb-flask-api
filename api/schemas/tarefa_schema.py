from api import ma
from ..models import tarefa_model
from marshmallow import fields

class TarefaSchema(ma.ModelSchema):
    class Meta:
        model = tarefa_model.Tarefa
        fields = ("id", "titulo", "descricao", "data_expiracao", "projeto")

    titulo = fields.String(required=True)
    descricao = fields.String(required=True)
    data_expiracao = fields.Date(required=True)
    projeto = fields.String(required=True)