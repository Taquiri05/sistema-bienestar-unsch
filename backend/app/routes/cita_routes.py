from flask import Blueprint, request, jsonify
from app import db
from app.models.cita import Cita
from app.models.estudiante import Estudiante
from app.models.personal_salud import PersonalSalud

bp = Blueprint("citas", __name__, url_prefix="/api/citas")


# ====================================================
# 1. CREAR CITA (Estudiante)
# ====================================================
@bp.route("/", methods=["POST"])
def crear_cita():
    data = request.get_json()

    idEstudiante = data.get("idEstudiante")
    especialidad = data.get("especialidad")
    fecha = data.get("fechaCita")
    hora = data.get("horaCita")

    if not idEstudiante or not especialidad or not fecha or not hora:
        return jsonify({"error": "Todos los campos son obligatorios"}), 400

    if not Estudiante.query.get(idEstudiante):
        return jsonify({"error": "El estudiante no existe"}), 404

    nueva_cita = Cita(
        idEstudiante=idEstudiante,
        especialidad=especialidad,
        fechaCita=fecha,
        horaCita=hora,
        estado="Pendiente"
    )

    db.session.add(nueva_cita)
    db.session.commit()

    return jsonify({"msg": "Cita creada correctamente"}), 201


# ====================================================
# 2. LISTAR CITAS PENDIENTES PARA PERSONAL DE SALUD
# ====================================================
@bp.route("/personal/<int:idPersonal>", methods=["GET"])
def citas_para_personal(idPersonal):

    personal = PersonalSalud.query.get(idPersonal)
    if not personal:
        return jsonify({"error": "El personal no existe"}), 404

    # Solo citas pendientes y que coincidan con la especialidad del personal
    citas = Cita.query.filter_by(
        especialidad=personal.especialidad,
        estado="Pendiente"
    ).all()

    lista = [{
        "idCita": c.idCita,
        "idEstudiante": c.idEstudiante,
        "especialidad": c.especialidad,
        "fechaCita": str(c.fechaCita),
        "horaCita": str(c.horaCita),
        "estado": c.estado
    } for c in citas]

    return jsonify(lista), 200



# ====================================================
# 3. MARCAR CITA COMO ATENDIDA
# ====================================================
@bp.route("/atender/<int:idCita>", methods=["PUT"])
def atender_cita(idCita):

    cita = Cita.query.get(idCita)
    if not cita:
        return jsonify({"error": "La cita no existe"}), 404

    cita.estado = "Atendida"
    db.session.commit()

    return jsonify({"msg": "Cita atendida correctamente"}), 200


# ====================================================
# 4. ESTADÍSTICAS PARA PERSONAL DE SALUD
# ====================================================
@bp.route("/estadisticas/personal/<int:idPersonal>", methods=["GET"])
def estadisticas_personal(idPersonal):

    personal = PersonalSalud.query.get(idPersonal)
    if not personal:
        return jsonify({"error": "El personal no existe"}), 404

    esp = personal.especialidad

    pendientes = Cita.query.filter_by(especialidad=esp, estado="Pendiente").count()
    atendidas = Cita.query.filter_by(especialidad=esp, estado="Atendida").count()
    canceladas = Cita.query.filter_by(especialidad=esp, estado="Cancelada").count()

    return jsonify({
        "pendientes": pendientes,
        "atendidas": atendidas,
        "canceladas": canceladas
    }), 200

# ====================================================
#  LISTAR CITAS DE UN ESTUDIANTE
# ====================================================
@bp.route("/estudiante/<int:idEstudiante>", methods=["GET"])
def listar_citas_estudiante(idEstudiante):

    # Verificar si existe el estudiante
    if not Estudiante.query.get(idEstudiante):
        return jsonify({"error": "El estudiante no existe"}), 404

    # Buscar todas sus citas
    citas = Cita.query.filter_by(idEstudiante=idEstudiante).all()

    lista = [{
        "idCita": c.idCita,
        "especialidad": c.especialidad,
        "fechaCita": str(c.fechaCita),
        "horaCita": str(c.horaCita),
        "estado": c.estado
    } for c in citas]

    return jsonify(lista), 200


# ====================================================
# 6. CANCELAR CITA (Estudiante)
# ====================================================
@bp.route("/<int:idCita>", methods=["DELETE"])
def cancelar_cita(idCita):

    cita = Cita.query.get(idCita)

    if not cita:
        return jsonify({"error": "La cita no existe"}), 404

    cita.estado = "Cancelada"
    db.session.commit()

    return jsonify({"msg": "Cita cancelada correctamente"}), 200


# ====================================================
# 5. ESTADÍSTICAS PARA ESTUDIANTE
# ====================================================
@bp.route("/estadisticas/<int:idEstudiante>", methods=["GET"])
def estadisticas_estudiante(idEstudiante):

    est = Estudiante.query.get(idEstudiante)
    if not est:
        return jsonify({"error": "El estudiante no existe"}), 404

    programadas = Cita.query.filter_by(idEstudiante=idEstudiante, estado="Pendiente").count()
    atendidas = Cita.query.filter_by(idEstudiante=idEstudiante, estado="Atendida").count()
    canceladas = Cita.query.filter_by(idEstudiante=idEstudiante, estado="Cancelada").count()

    return jsonify({
        "programadas": programadas,
        "atendidas": atendidas,
        "canceladas": canceladas
    }), 200

