"""
app.py

Este arquivo executa o servidor local.
Utiliza a função create_app() definida em main.py.
"""

from main import create_app
import config

app = create_app()

if __name__ == "__main__":
    app.run(
        debug=False,
        host=config.HOST,
        port=config.PORT
    )

