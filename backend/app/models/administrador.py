from app import db

class Administrador(db.Model):
    __tablename__ = "Administrador"

    idAdmin = db.Column(db.Integer, primary_key=True)
    idUsuario = db.Column(db.Integer, db.ForeignKey("Usuario.idUsuario"), nullable=False)

    area = db.Column(db.String(100))
    cargo = db.Column(db.String(100))

    reportes = db.relationship("Reporte", backref="admin", lazy=True)
