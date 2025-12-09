from app import db

class AtencionMedica(db.Model):
    __tablename__ = 'AtencionMedica'

    idAtencion = db.Column(db.Integer, primary_key=True)
    idCita = db.Column(db.Integer, db.ForeignKey('Cita.idCita'))
    idPersonal = db.Column(db.Integer, db.ForeignKey('PersonalSalud.idPersonal'))  # ← AQUÍ EL CAMBIO
    diagnostico = db.Column(db.Text)
    tratamiento = db.Column(db.Text)
    observacion = db.Column(db.Text)
    fechaAtencion = db.Column(db.DateTime)

    personal = db.relationship('PersonalSalud', backref='atenciones')
    cita = db.relationship('Cita', backref='atencion')
