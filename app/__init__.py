from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.extensions import bcrypt, jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)

    # init extensions
    bcrypt.init_app(app)
    jwt.init_app(app)

    from app.routes.auth_routes import auth_bp
    from app.routes.admin_routes import admin_bp
    from app.routes.hr_routes import hr_bp
    from app.routes.employee_routes import employee_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(hr_bp)
    app.register_blueprint(employee_bp)

    return app

