from functools import wraps
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify

def role_required(required_role):
    def wrapper(fn):
        @wraps(fn)
        @jwt_required()
        def decorator(*args, **kwargs):
            user = get_jwt_identity()
            if user["role"] != required_role:
                return jsonify({"message": "Access forbidden"}), 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper
