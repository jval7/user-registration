from flask import Flask
from flask_migrate import Migrate
from app.models.db import db
from app.routes.user_bp import user_bp
import click
from flask.cli import with_appcontext
from app.models.db import db

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)
    migrate.init_app(app, db)
    app.register_blueprint(user_bp)
    app.cli.add_command(init_db_command)
    return app

def init_db():
    db.drop_all()
    db.create_all()


@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db()
    click.echo("Initialized the database.")