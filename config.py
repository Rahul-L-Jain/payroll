class Config:
    SECRET_KEY = "super-secret-key"  
    # already present ✅
    JWT_ALGORITHM = "HS256"
    JWT_SECRET_KEY = "jwt-super-secret-key"

    DB_HOST = "localhost"
    DB_USER = "root"
    DB_PASSWORD = "root"
    DB_NAME = "payroll_db"

