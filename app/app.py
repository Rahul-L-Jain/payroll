from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.utils.db import close_db

from app.routes.auth_routes import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)

    app.teardown_appcontext(close_db)

    app.register_blueprint(auth_bp)

    @app.route("/health", methods=["GET"])
    def health():
        return {"status": "ok"}, 200

    return app

