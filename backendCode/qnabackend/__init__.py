from flask import Flask
from qnabackend.config import Config
from flask_cors import CORS

def create_app(config_class = Config):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_class)
    from qnabackend.resources.routes import resources
    app.register_blueprint(resources)

    return app