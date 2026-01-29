from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from app.config import Config

bcrypt = Bcrypt()  # shared bcrypt instance

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Enable CORS
    CORS(app)

    # Init bcrypt
    bcrypt.init_app(app)

    # Register blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.admin_routes import admin_bp
    from app.routes.hr_routes import hr_bp
    from app.routes.employee_routes import employee_bp
    from app.routes.home_routes import home_bp   # ✅ ADDED

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(hr_bp)
    app.register_blueprint(employee_bp)
    app.register_blueprint(home_bp)               # ✅ ADDED

    return app

