from app import db

class Perfil(db.Model):
    __tablename__ = "Perfil"

    idPerfil = db.Column(db.Integer, primary_key=True)
    direccion = db.Column(db.String(255))
    dni = db.Column(db.String(20))
    fechaNacimiento = db.Column(db.Date)
    genero = db.Column(db.String(20))
    telefono = db.Column(db.String(20))
