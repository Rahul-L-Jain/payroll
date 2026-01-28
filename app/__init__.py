from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)

# Import config
from app.config import Config
app.config['SECRET_KEY'] = Config.SECRET_KEY

# Enable CORS
CORS(app)

# Initialize Bcrypt for password hashing
bcrypt = Bcrypt(app)

# Import routes (must be after app creation)
from app.routes import auth_routes, admin_routes, hr_routes, employee_routes

# Register Blueprints (if using blueprints)
app.register_blueprint(auth_routes.auth_bp)
app.register_blueprint(admin_routes.admin_bp)
app.register_blueprint(hr_routes.hr_bp)
app.register_blueprint(employee_routes.employee_bp)

