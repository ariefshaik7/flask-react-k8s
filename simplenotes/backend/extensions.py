# AFTER
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from prometheus_flask_exporter import PrometheusMetrics
from flask_jwt_extended import JWTManager # <-- IMPORT THIS

db = SQLAlchemy()
bcrypt = Bcrypt()
cors = CORS()
metrics = PrometheusMetrics.for_app_factory()
jwt = JWTManager() # <-- ADD THIS LINE