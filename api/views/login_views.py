from api import api
from flask_restful import Resource
from ..schemas.login_schema import LoginSchema
from flask import request, make_response, jsonify
from ..services import usuario_service
from ..models import usuario_model
from flask_jwt_extended import create_access_token
from datetime import timedelta


class LoginList(Resource):
    def post(self):
        ls = LoginSchema()
        validate = ls.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            email = request.json["email"]
            senha = request.json["senha"]
            usuario_bd = usuario_service.listar_usuario(email)
            if usuario_bd and usuario_bd.ver_senha(senha):
                access_token = create_access_token(
                    identity=usuario_bd.id,
                    expires_delta=timedelta(seconds=60)
                )
                return make_response(jsonify({
                    'access_token': access_token,
                    'message': 'login realizado com sucesso'
                }), 200)
            return make_response(jsonify({
                'message': 'Credenciais inválidas'
            }), 401)

api.add_resource(LoginList, '/login')