from app import db

class Usuario(db.Model):
    __tablename__ = "Usuario"

    idUsuario = db.Column(db.Integer, primary_key=True)
    contrasena = db.Column(db.String(255), nullable=False)
    correo = db.Column(db.String(100), nullable=False, unique=True)
    isUser = db.Column(db.Integer, default=1)
    tipoUsuario = db.Column(db.String(50), nullable=False)

    idPerfil = db.Column(db.Integer, db.ForeignKey("Perfil.idPerfil"))
    idRol = db.Column(db.Integer, db.ForeignKey("Rol.idRol"))
