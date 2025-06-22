from flask import Flask
from .config import Config
from .extensions import db, migrate, jwt, mail
from .routes import register_blueprints
from flask_cors import CORS


def create_app(config_class=Config):
    app = Flask(__name__)
    # cors = CORS(app, resources={r"/*": {"origins": "*"}})
    CORS(app)
    app.config.from_object(config_class)

    # Initialize extensions
    jwt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    # Automatically create tables
    with app.app_context():
        # db.drop_all()
        db.create_all()

    # Register blueprints
    register_blueprints(app)

    return app
