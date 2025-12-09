from flask import Blueprint, request, jsonify
from app import db
from app.models.derivacion import Derivacion
from app.models.atencion import AtencionMedica

bp = Blueprint("derivaciones", __name__, url_prefix="/api/derivaciones")

# Crear derivación
@bp.route("/", methods=["POST"])
def crear_derivacion():
    data = request.json

    idAtencion = data.get("idAtencion")
    especialidadDestino = data.get("especialidadDestino")
    comentarios = data.get("comentarios")

    atencion = AtencionMedica.query.get(idAtencion)
    if not atencion:
        return jsonify({"error": "Atención no encontrada"}), 404

    derivacion = Derivacion(
        idAtencion=idAtencion,
        especialidadDestino=especialidadDestino,
        comentarios=comentarios
    )

    db.session.add(derivacion)
    db.session.commit()

    return jsonify({
        "msg": "Derivación registrada correctamente",
        "idDerivacion": derivacion.idDerivacion
    }), 201


# 🔥 LISTAR TODAS LAS DERIVACIONES
@bp.route("/", methods=["GET"])
def listar_derivaciones():
    derivaciones = Derivacion.query.all()

    resultado = []
    for d in derivaciones:
        resultado.append({
            "idDerivacion": d.idDerivacion,
            "idAtencion": d.idAtencion,
            "especialidadDestino": d.especialidadDestino,
            "comentarios": d.comentarios
        })

    return jsonify(resultado), 200


# 🔥 LISTAR DERIVACIONES POR ID DE ATENCIÓN
@bp.route("/atencion/<int:idAtencion>", methods=["GET"])
def listar_derivacion_por_atencion(idAtencion):
    derivaciones = Derivacion.query.filter_by(idAtencion=idAtencion).all()

    if not derivaciones:
        return jsonify({"error": "No hay derivaciones para esta atención"}), 404

    resultado = []
    for d in derivaciones:
        resultado.append({
            "idDerivacion": d.idDerivacion,
            "especialidadDestino": d.especialidadDestino,
            "comentarios": d.comentarios
        })

    return jsonify(resultado), 200


# 🔥 Obtener una derivación por ID
@bp.route("/<int:idDerivacion>", methods=["GET"])
def obtener_derivacion(idDerivacion):
    derivacion = Derivacion.query.get(idDerivacion)

    if not derivacion:
        return jsonify({"error": "Derivación no encontrada"}), 404

    return jsonify({
        "idDerivacion": derivacion.idDerivacion,
        "idAtencion": derivacion.idAtencion,
        "especialidadDestino": derivacion.especialidadDestino,
        "comentarios": derivacion.comentarios
    }), 200


# 🔧 Actualizar derivación
@bp.route("/<int:idDerivacion>", methods=["PUT"])
def actualizar_derivacion(idDerivacion):
    data = request.json
    derivacion = Derivacion.query.get(idDerivacion)

    if not derivacion:
        return jsonify({"error": "Derivación no encontrada"}), 404

    derivacion.especialidadDestino = data.get("especialidadDestino", derivacion.especialidadDestino)
    derivacion.comentarios = data.get("comentarios", derivacion.comentarios)

    db.session.commit()

    return jsonify({
        "msg": "Derivación actualizada correctamente",
        "idDerivacion": derivacion.idDerivacion
    }), 200


#  Eliminar una derivación
@bp.route("/<int:idDerivacion>", methods=["DELETE"])
def eliminar_derivacion(idDerivacion):
    derivacion = Derivacion.query.get(idDerivacion)
    if not derivacion:
        return jsonify({"error": "Derivación no encontrada"}), 404

    db.session.delete(derivacion)
    db.session.commit()

    return jsonify({
        "msg": "Derivación eliminada correctamente",
        "idDerivacion": idDerivacion
    }), 200
