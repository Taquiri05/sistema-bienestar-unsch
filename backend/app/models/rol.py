from app import db

class Rol(db.Model):
    __tablename__ = "Rol"

    idRol = db.Column(db.Integer, primary_key=True)
    nombreRol = db.Column(db.String(50), nullable=False)
    permisos = db.Column(db.String(255))
