from app import db

class Derivacion(db.Model):
    __tablename__ = "Derivacion"

    idDerivacion = db.Column(db.Integer, primary_key=True)
    idAtencion = db.Column(db.Integer, db.ForeignKey("AtencionMedica.idAtencion"), nullable=False)

    especialidadDestino = db.Column(db.String(100))
    fechaDerivacion = db.Column(db.Date)
    comentarios = db.Column(db.Text)
