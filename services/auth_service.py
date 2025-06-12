"""
auth_service.py

Este módulo contém a lógica de autenticação usada pela rota /login.
Embora o sistema seja propositalmente vulnerável, esta separação mostra
como separar responsabilidades: rotas lidam com entrada e resposta,
e os serviços lidam com lógica de negócio (mesmo que simplificada).
"""

def check_login(username: str, password: str) -> bool:
    """
    Verifica se o usuário e senha correspondem aos dados esperados.

    ⚠️ Vulnerável propositalmente: não há hash, não há banco de dados,
    e os dados estão hardcoded.
    """
    return username == "admin" and password == "1234"
