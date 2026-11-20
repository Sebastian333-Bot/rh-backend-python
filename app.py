import os
from flask import Flask
from flask_cors import CORS

from extensions import db, migrate, ma
from api import bp as api_bp
import api.empleados  # asegura que las rutas se registren
import models  # asegura que los modelos estén visibles para Alembic/Flask-Migrate


def create_app():
    app = Flask(__name__)

    # Ajusta usuario/contraseña/host según tu entorno
    db_host = os.getenv("DB_HOST", "mysql-db")
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+pymysql://root:admin@{db_host}/recursos_humanos_db?charset=utf8mb4"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_AS_ASCII"] = False

    # Extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    # Blueprints
    app.register_blueprint(api_bp)

    # CORS: permite peticiones desde cualquier origen (incluyendo http://18.191.21.84:4200)
    # Se inicializa después de registrar el blueprint de Flask-RESTful para que también
    # incluya cabeceras CORS en respuestas de error manejadas por la API.
    CORS(
        app,
        resources={
            r"/*": {
                "origins": "*",
                "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                "allow_headers": "*",
            }
        },
    )

    @app.get("/")
    def home():
        return "API de Recursos Humanos (Flask) ✅"

    return app


if __name__ == "__main__":
    create_app().run(host='0.0.0.0', debug=True, port=8080)

