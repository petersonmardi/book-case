from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    key_value = []
    random_key = os.urandom(16)
    key_value.append(random_key)

    app.config.from_mapping(
        SECRET_KEY=key_value[0],
    )
    @app.route('/hello')
    def hello():
        return """</h1>¡Hola! 
               Estamos probando 
               nuestra app.<h1>"""

    from . import index
    app.register_blueprint(index.bp)

    return app
