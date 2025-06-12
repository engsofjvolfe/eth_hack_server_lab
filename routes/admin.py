from flask import Blueprint
from services.admin_service import get_admin_content

bp = Blueprint("admin", __name__)

@bp.route("/admin")
def admin():
    """
    Rota de administração.

    Aqui seria necessário algum tipo de verificação de autenticação,
    mas ela está ausente propositalmente. Ideal para testes de acesso
    não autorizado e exploração da falta de proteção.
    """
    return get_admin_content()
