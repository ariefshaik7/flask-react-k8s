from flask import Flask, Response
from flask_cors import CORS
from .config import Config
from .extensions import db, jwt
from .routes.auth import bp as auth_bp
from .routes.notes import bp as notes_bp
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import generate_latest

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    CORS(app)

    metrics = PrometheusMetrics(app)

    app.register_blueprint(auth_bp, url_prefix='/api')
    app.register_blueprint(notes_bp, url_prefix='/api')

    @app.route('/metrics')
    def metrics_endpoint():
        return Response(generate_latest(), mimetype='text/plain')

    return app
