from flask import Flask
from config import Config
from extensions import db, bcrypt, cors, metrics
from routes import auth, notes

def create_app():
    app = Flask(__name__)
    metrics.init_app(app)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app)

    # Register blueprints
    app.register_blueprint(auth.bp)
    app.register_blueprint(notes.bp)

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5001, debug=True)
