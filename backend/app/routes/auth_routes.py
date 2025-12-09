from flask import Blueprint, request, jsonify
from app import db
from app.models.usuario import Usuario
from app.models.estudiante import Estudiante
from app.models.personal_salud import PersonalSalud
from app.models.administrador import Administrador
from app.models.perfil import Perfil

bp = Blueprint("auth", __name__, url_prefix="/api/auth")


# ============================================================
#   REGISTRO DE USUARIO
# ============================================================
@bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    print("\n=== LLEGÓ AL BACKEND / REGISTER ===")
    print("DATA:", data)

    nombre = data.get("nombre")
    apellido = data.get("apellido")
    dni = data.get("dni")
    correo = data.get("correo")
    contrasena = data.get("contrasena")
    tipoUsuario = data.get("tipoUsuario")

    if not nombre or not apellido or not dni or not correo or not contrasena:
        return jsonify({"error": "Datos incompletos"}), 400

    if Usuario.query.filter_by(correo=correo).first():
        return jsonify({"error": "El correo ya está registrado"}), 409

    # ===============================
    # CREAR PERFIL
    # ===============================
    perfil = Perfil(
        dni=dni,
        direccion=None,
        fechaNacimiento=None,
        genero=None,
        telefono=None
    )
    db.session.add(perfil)
    db.session.commit()

    # ===============================
    # CREAR USUARIO
    # ===============================
    usuario = Usuario(
        correo=correo,
        contrasena=contrasena,
        tipoUsuario=tipoUsuario,
        idPerfil=perfil.idPerfil,
        idRol=1
    )
    db.session.add(usuario)
    db.session.commit()

    # ===============================
    # CREAR REGISTRO SEGÚN TIPO
    # ===============================
    if tipoUsuario == "estudiante":
        nuevo = Estudiante(
            idUsuario=usuario.idUsuario,
            nombre=nombre,
            apellido=apellido,
            codigo=data.get("codigo"),
            escuela=data.get("escuela"),
            ciclo=data.get("ciclo")
        )

    elif tipoUsuario == "personal":
        nuevo = PersonalSalud(
            idUsuario=usuario.idUsuario,
            especialidad=data.get("especialidad")
        )

    elif tipoUsuario == "administrador":
        nuevo = Administrador(
            idUsuario=usuario.idUsuario,
            area=data.get("area"),
            cargo=data.get("cargo")
        )

    db.session.add(nuevo)
    db.session.commit()

    return jsonify({
        "msg": "Usuario registrado correctamente",
        "idUsuario": usuario.idUsuario
    }), 201



# ============================================================
#   LOGIN
# ============================================================
@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    print("\n=== LLEGÓ AL BACKEND / LOGIN ===")
    print("DATA:", data)

    correo = data.get("correo")
    contrasena = data.get("contrasena")

    if not correo or not contrasena:
        return jsonify({"error": "Faltan datos"}), 400

    usuario = Usuario.query.filter_by(correo=correo).first()

    if not usuario:
        return jsonify({"error": "Correo no encontrado"}), 404

    if usuario.contrasena != contrasena:
        return jsonify({"error": "Contraseña incorrecta"}), 401

    # Identificar tipo de usuario
    tipo = usuario.tipoUsuario.lower()
    rolID = None

    if tipo == "estudiante":
        obj = Estudiante.query.filter_by(idUsuario=usuario.idUsuario).first()
        rolID = obj.idEstudiante if obj else None

    elif tipo == "personal":
        obj = PersonalSalud.query.filter_by(idUsuario=usuario.idUsuario).first()
        rolID = obj.idPersonal if obj else None

    elif tipo == "administrador":
        obj = Administrador.query.filter_by(idUsuario=usuario.idUsuario).first()
        rolID = obj.idAdmin if obj else None

    return jsonify({
        "msg": "Login correcto",
        "idUsuario": usuario.idUsuario,
        "tipoUsuario": usuario.tipoUsuario,
        "rolID": rolID
    }), 200
