from app import db
from datetime import datetime

class HistorialMedico(db.Model):
    __tablename__ = "HistorialMedico"

    idHistorial = db.Column(db.Integer, primary_key=True)
    idEstudiante = db.Column(db.Integer, db.ForeignKey("Estudiante.idEstudiante"), nullable=False)

    descripcion = db.Column(db.Text)
    fechaRegistro = db.Column(db.DateTime, default=datetime.utcnow)
