import datetime
import jwt
from flask import current_app

def generar_token(data):
    payload = {
        "data": data,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }

    token = jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")
    return token


def verificar_token(token):
    try:
        data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
        return data
    except Exception:
        return None
