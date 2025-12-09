from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import Config
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Habilitar CORS
    CORS(app)

    # Inicializar DB
    db.init_app(app)

    # ===============================
    # IMPORTAR MODELOS ANTES DE create_all
    # ===============================
    with app.app_context():
        from app.models.usuario import Usuario
        from app.models.perfil import Perfil
        from app.models.rol import Rol
        from app.models.estudiante import Estudiante
        from app.models.personal_salud import PersonalSalud
        from app.models.administrador import Administrador
        from app.models.cita import Cita
        from app.models.historial import HistorialMedico
        from app.models.atencion import AtencionMedica
        from app.models.derivacion import Derivacion
        from app.models.reporte import Reporte

        db.create_all()

    # ===============================
    # REGISTRO DE BLUEPRINTS
    # ===============================
    from app.routes.user_routes import bp as user_bp
    from app.routes.usuario_routes import bp as usuario_bp
    from app.routes.cita_routes import bp as cita_bp
    from app.routes.derivacion_routes import bp as derivacion_bp
    from app.routes.atencion_routes import bp as atencion_bp
    from app.routes.historial_routes import bp as historial_bp
    from app.routes.reporte_routes import bp as reporte_bp
    from app.routes.auth_routes import bp as auth_bp

    app.register_blueprint(user_bp)
    app.register_blueprint(usuario_bp)
    app.register_blueprint(cita_bp)
    app.register_blueprint(derivacion_bp)
    app.register_blueprint(atencion_bp)
    app.register_blueprint(historial_bp)
    app.register_blueprint(reporte_bp)
    app.register_blueprint(auth_bp)

    return app
