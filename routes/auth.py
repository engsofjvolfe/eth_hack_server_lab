from flask import Blueprint, request, redirect, url_for
from services.auth_service import check_login

bp = Blueprint("auth", __name__)

@bp.route("/login", methods=["POST", "GET"])
def login():
    """
    Rota de login.

    Recebe dados do formulário e envia para o serviço de autenticação.
    A resposta é direta, sem redirecionamento, cookies ou sessão,
    intencionalmente vulnerável para testes.
    """
    if request.method == "GET":
        return '''
            <form method="post">
                <input type="text" name="username" placeholder="Usuário">
                <input type="password" name="password" placeholder="Senha">
                <button type="submit">Entrar</button>
            </form>
        '''

    username = request.form.get("username")
    password = request.form.get("password")

    if check_login(username, password):
        return "Bem-vindo, admin!"

    return "Credenciais inválidas"
