from app import db

class Reporte(db.Model):
    __tablename__ = "Reporte"

    idReporte = db.Column(db.Integer, primary_key=True)
    idAdmin = db.Column(db.Integer, db.ForeignKey("Administrador.idAdmin"), nullable=False)

    direccion = db.Column(db.String(255))
    dni = db.Column(db.String(20))
    fechaNacimiento = db.Column(db.Date)
    genero = db.Column(db.String(20))
    telefono = db.Column(db.String(20))
