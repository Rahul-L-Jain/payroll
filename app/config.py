class Config:
    SECRET_KEY = "super-secret-key-change-this"

    JWT_SECRET_KEY = "jwt-secret-key-change-this"  # ✅ REQUIRED
    JWT_ACCESS_TOKEN_EXPIRES = 60 * 60 * 8        # 8 hours
    DB_HOST = "localhost"
    DB_USER = "root"
    DB_PASSWORD = "root"
    DB_NAME = "payroll_db"


