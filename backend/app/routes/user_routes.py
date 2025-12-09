from flask import Blueprint, jsonify

bp = Blueprint('user_routes', __name__, url_prefix='/api/test')

@bp.route('/', methods=['GET'])
def test_route():
    return jsonify({"msg": "Ruta de prueba funcionando"})
