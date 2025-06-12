"""
main.py

Este arquivo define a função create_app(), que inicializa
e configura a aplicação Flask, registrando rotas e carregando
as configurações externas.

Esse padrão é comum em projetos reais, pois permite separar
a inicialização do servidor do código principal (ex: testes).
"""

from flask import Flask
from routes.auth import bp as auth_bp
from routes.admin import bp as admin_bp
import config

def create_app() -> Flask:
    """
    Cria e configura a aplicação Flask.
    """
    app = Flask(__name__)
    app.secret_key = config.SECRET_KEY

    # Registrar rotas (blueprints)
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)

    return app
