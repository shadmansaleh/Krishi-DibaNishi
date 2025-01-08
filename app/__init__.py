from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.routes.views import pages, register_pages
from app.routes.api import api
from app.extensions import db
from app.utils import maybe_compile_scss

migrate = Migrate()

def create_app():
    maybe_compile_scss("bootstrap_custom.scss")

    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)


    from .routes.auth import auth
    app.register_blueprint(auth)
    app.register_blueprint(api)

    # Register the Blueprint
    app.register_blueprint(pages)
    register_pages(app)

    # Catch-all route for 404 errors
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("errors/404.html"), 404


    return app

