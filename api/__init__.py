from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

api = Api(app)

from .views import tarefa_views, projeto_views, funcionario_views, usuario_views
from .models import tarefa_model, projeto_model, funcionario_model, usuario_model