import os
from dotenv import load_dotenv

# Cargar el archivo .env
load_dotenv()

class Config:
    SECRET_KEY = "clave-secreta-unsch"

    # Configuración de la base de datos MySQL
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
