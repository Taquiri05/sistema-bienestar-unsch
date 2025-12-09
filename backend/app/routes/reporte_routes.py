from flask import Blueprint, request, jsonify
from app import db
from app.models.reporte import Reporte

bp = Blueprint('reporte_routes', __name__, url_prefix='/api/reportes')


# ================================
# CREAR REPORTE
# ================================
@bp.route('/', methods=['POST'])
def crear_reporte():
    data = request.get_json()

    # Validación mínima
    if "idAdmin" not in data:
        return jsonify({"error": "idAdmin es obligatorio"}), 400

    nuevo = Reporte(
        idAdmin=data["idAdmin"],
        direccion=data.get("direccion"),
        dni=data.get("dni"),
        fechaNacimiento=data.get("fechaNacimiento"),
        genero=data.get("genero"),
        telefono=data.get("telefono")
    )

    db.session.add(nuevo)
    db.session.commit()

    return jsonify({
        "msg": "Reporte creado correctamente",
        "idReporte": nuevo.idReporte
    }), 201


# ================================
# LISTAR TODOS LOS REPORTES
# ================================
@bp.route('/', methods=['GET'])
def listar_reportes():
    reportes = Reporte.query.all()

    resultado = [
        {
            "idReporte": r.idReporte,
            "idAdmin": r.idAdmin,
            "direccion": r.direccion,
            "dni": r.dni,
            "fechaNacimiento": str(r.fechaNacimiento),
            "genero": r.genero,
            "telefono": r.telefono
        }
        for r in reportes
    ]

    return jsonify(resultado), 200


# ================================
# OBTENER REPORTE POR ID
# ================================
@bp.route('/<int:idReporte>', methods=['GET'])
def obtener_reporte(idReporte):
    r = Reporte.query.get(idReporte)

    if not r:
        return jsonify({"error": "Reporte no encontrado"}), 404

    return jsonify({
        "idReporte": r.idReporte,
        "idAdmin": r.idAdmin,
        "direccion": r.direccion,
        "dni": r.dni,
        "fechaNacimiento": str(r.fechaNacimiento),
        "genero": r.genero,
        "telefono": r.telefono
    }), 200


# ================================
# ACTUALIZAR REPORTE
# ================================
@bp.route('/<int:idReporte>', methods=['PUT'])
def actualizar_reporte(idReporte):
    r = Reporte.query.get(idReporte)

    if not r:
        return jsonify({"error": "Reporte no encontrado"}), 404

    data = request.get_json()

    r.direccion = data.get("direccion", r.direccion)
    r.dni = data.get("dni", r.dni)
    r.fechaNacimiento = data.get("fechaNacimiento", r.fechaNacimiento)
    r.genero = data.get("genero", r.genero)
    r.telefono = data.get("telefono", r.telefono)

    db.session.commit()

    return jsonify({
        "msg": "Reporte actualizado correctamente",
        "idReporte": r.idReporte
    }), 200


# ================================
# ELIMINAR REPORTE
# ================================
@bp.route('/<int:idReporte>', methods=['DELETE'])
def eliminar_reporte(idReporte):
    r = Reporte.query.get(idReporte)

    if not r:
        return jsonify({"error": "Reporte no encontrado"}), 404

    db.session.delete(r)
    db.session.commit()

    return jsonify({"msg": "Reporte eliminado correctamente"}), 200
