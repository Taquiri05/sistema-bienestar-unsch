from app import db

class Estudiante(db.Model):
    __tablename__ = "Estudiante"

    idEstudiante = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idUsuario = db.Column(db.Integer, db.ForeignKey("Usuario.idUsuario"), nullable=False)

    # NUEVOS CAMPOS
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))

    # CAMPOS QUE YA TENÍAS EN TU BD
    codigo = db.Column(db.String(20))
    escuela = db.Column(db.String(150))
    ciclo = db.Column(db.String(10))

    citas = db.relationship("Cita", backref="estudiante", lazy=True)
    historial = db.relationship("HistorialMedico", backref="estudiante", lazy=True)

dni = db.Column(db.String(20))
nombre = db.Column(db.String(100))
apellido = db.Column(db.String(100))
