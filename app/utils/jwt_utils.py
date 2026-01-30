import jwt
from datetime import datetime, timedelta
from app.config import Config

def generate_token(user_id, role):
    payload = {
        "user_id": user_id,
        "role": role,
        "exp": datetime.utcnow() + timedelta(hours=2)
    }
    token = jwt.encode(payload, Config.SECRET_KEY, algorithm=Config.JWT_ALGORITHM)
    return token


def decode_token(token):
    return jwt.decode(token, Config.SECRET_KEY, algorithms=[Config.JWT_ALGORITHM])
