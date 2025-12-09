from flask import Blueprint, request, jsonify
from app import db
from app.models.atencion import AtencionMedica
from datetime import datetime

bp = Blueprint('atencion_routes', __name__, url_prefix='/api/atenciones')


@bp.route('/', methods=['POST'])
def registrar_atencion():
    data = request.get_json()

    nueva_atencion = AtencionMedica(
        idCita=data['idCita'],
        idPersonal=data['idPersonal'],
        diagnostico=data.get('diagnostico'),
        tratamiento=data.get('tratamiento'),
        observacion=data.get('observacion'),
        fechaAtencion=datetime.now()
    )

    db.session.add(nueva_atencion)
    db.session.commit()

    return jsonify({
        "msg": "Atención registrada correctamente",
        "idAtencion": nueva_atencion.idAtencion
    }), 201


@bp.route('/<int:id>', methods=['GET'])
def obtener_atencion(id):
    atencion = AtencionMedica.query.get(id)

    if not atencion:
        return jsonify({"error": "Atención no encontrada"}), 404

    return jsonify({
        "idAtencion": atencion.idAtencion,
        "idCita": atencion.idCita,
        "idPersonal": atencion.idPersonal,
        "diagnostico": atencion.diagnostico,
        "tratamiento": atencion.tratamiento,
        "observacion": atencion.observacion,
        "fechaAtencion": str(atencion.fechaAtencion)
    })
