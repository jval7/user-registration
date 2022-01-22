from flask import Flask
from flask_migrate import Migrate
from app.models.db import db
from app.routes.user_bp import user_bp


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)
    migrate.init_app(app, db)
    app.register_blueprint(user_bp)
    return app
