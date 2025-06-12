"""
config.py

Contém configurações básicas da aplicação. Ideal para isolar variáveis
que podem ser modificadas em diferentes ambientes (desenvolvimento,
teste, produção, etc.).

Neste projeto, as configurações são propositalmente fracas para facilitar
o estudo de vulnerabilidades.
"""

SECRET_KEY = "super_inseguro"
DEBUG = True
HOST = "0.0.0.0"
PORT = 5000
