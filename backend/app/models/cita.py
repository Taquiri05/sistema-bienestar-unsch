from app import db

class Cita(db.Model):
    __tablename__ = "Cita"

    idCita = db.Column(db.Integer, primary_key=True)
    idEstudiante = db.Column(db.Integer, db.ForeignKey("Estudiante.idEstudiante"), nullable=False)

    especialidad = db.Column(db.String(100), nullable=False)
    fechaCita = db.Column(db.Date, nullable=False)
    horaCita = db.Column(db.Time, nullable=False)
    estado = db.Column(db.String(50))
