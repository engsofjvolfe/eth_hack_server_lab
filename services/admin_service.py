"""
admin_service.py

Este módulo simula uma função protegida que deveria ser acessada apenas
por usuários autenticados. Aqui está aberta de propósito para estudo.

Se fosse um sistema real, esse serviço verificaria sessão, JWT, etc.
"""

def get_admin_content() -> str:
    """
    Retorna o conteúdo 'restrito', sem qualquer verificação de segurança.
    """
    return "Área restrita... ou deveria ser 😬"
