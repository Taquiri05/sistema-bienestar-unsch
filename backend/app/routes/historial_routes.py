from flask import Blueprint, jsonify
from app.models.perfil import Perfil
from app.models.estudiante import Estudiante
from app.models.historial import HistorialMedico

bp = Blueprint("historial_routes", __name__, url_prefix="/api/historial")

# ======================================================
#  BUSCAR HISTORIAL POR DNI
# ======================================================
@bp.route("/buscar/<dni>", methods=["GET"])
def buscar_estudiante(dni):

    # 1. Buscar perfil por DNI
    perfil = Perfil.query.filter_by(dni=dni).first()

    if not perfil:
        return jsonify({"error": "No existe estudiante con ese DNI"}), 404

    # 2. Buscar estudiante por idPerfil
    estudiante = Estudiante.query.join(Perfil, Perfil.idPerfil == Estudiante.idUsuario)\
                                 .filter(Perfil.dni == dni).first()

    if not estudiante:
        estudiante = Estudiante.query.filter_by(idUsuario=perfil.idPerfil).first()

    if not estudiante:
        return jsonify({"error": "No existe estudiante asociado a ese DNI"}), 404

    # 3. Buscar historial médico
    historial = HistorialMedico.query.filter_by(idEstudiante=estudiante.idEstudiante).all()

    historial_lista = [{
        "descripcion": h.descripcion,
        "fecha": h.fechaRegistro.strftime("%Y-%m-%d %H:%M")
    } for h in historial]

    # 4. Respuesta final
    return jsonify({
        "estudiante": {
            "nombre": estudiante.nombre,
            "apellido": estudiante.apellido,
            "codigo": estudiante.codigo,
            "escuela": estudiante.escuela,
            "ciclo": estudiante.ciclo
        },
        "historial": historial_lista
    }), 200
