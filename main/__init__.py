from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
bcrypt = Bcrypt()
login = LoginManager()
login.login_view = "main.login"


def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    initialize_extensions(app)
    register_blueprints(app)
    return app


def initialize_extensions(app):
    db.init_app(app)
    bcrypt.init_app(app)
    login.init_app(app)

    @app.before_first_request
    def create_table():
        db.create_all()

    from main.models import User

    @login.user_loader
    def load_user(user_id):
        return User.query.filter(User.id == int(user_id)).first()


def register_blueprints(app):
    from main.rest import blueprint
    app.register_blueprint(blueprint, url_prefix='/api')

    from main.uiapp import bp
    app.register_blueprint(bp)

