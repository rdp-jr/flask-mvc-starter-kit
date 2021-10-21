from flask import Flask, render_template
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from app.models import db
from app.utils import register_error_handlers, register_blueprints

flask_bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "users.login"


def init_app(testing=False):
    app = Flask(__name__, template_folder="views", static_folder="public")
    app.config.from_pyfile("config.py")

    with app.app_context():
        # include routes
        @app.get("/")
        def welcome():
            return render_template("welcome.html")

        register_extensions(app)
        register_blueprints(app)
        register_error_handlers(app)
        db.create_all()

        return app


def register_extensions(app):
    db.init_app(app)
    flask_bcrypt.init_app(app)
    login_manager.init_app(app)
