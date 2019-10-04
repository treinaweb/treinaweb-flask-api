from api import ma
from ..models import funcionario_model
from marshmallow import fields

class FuncionarioSchema(ma.ModelSchema):
    class Meta:
        model = funcionario_model.Funcionario
        fields = ("id", "nome", "idade", "projetos")

    nome = fields.String(required=True)
    idade = fields.Integer(required=True)
