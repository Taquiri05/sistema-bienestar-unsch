from app import db

class PersonalSalud(db.Model):
    __tablename__ = "PersonalSalud"

    idPersonal = db.Column(db.Integer, primary_key=True)
    idUsuario = db.Column(db.Integer, db.ForeignKey("Usuario.idUsuario"), nullable=False)

    especialidad = db.Column(db.String(100))
    nroColegiatura = db.Column(db.String(50))

    # RELACIÓN CORRECTA
    usuario = db.relationship("Usuario", backref="personal_salud", uselist=False)
