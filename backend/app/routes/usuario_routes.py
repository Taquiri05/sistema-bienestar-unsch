from flask import Blueprint, jsonify

bp = Blueprint('usuario_routes', __name__, url_prefix='/api/usuarios')

@bp.route('/', methods=['GET'])
def listar_usuarios():
    return jsonify({"msg": "Usuarios funcionando"})
