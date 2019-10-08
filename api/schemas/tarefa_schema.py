from api import ma
from ..models import tarefa_model
from marshmallow import fields

class TarefaSchema(ma.ModelSchema):
    class Meta:
        model = tarefa_model.Tarefa
        fields = ("id", "titulo", "descricao", "data_expiracao", "projeto", "_links")

    titulo = fields.String(required=True)
    descricao = fields.String(required=True)
    data_expiracao = fields.Date(required=True)
    projeto = fields.String(required=True)
    _links = ma.Hyperlinks(
        {
            "get": ma.URLFor("tarefadetail", id="<id>"),
            "put": ma.URLFor("tarefadetail", id="<id>"),
            "delete": ma.URLFor("tarefadetail", id="<id>"),

        }
    )