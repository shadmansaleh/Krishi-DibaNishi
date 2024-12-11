from flask import Flask
from app.routes.views import pages, register_pages
from app.routes.api import api
from app.routes.auth import auth

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Register the Blueprint
    app.register_blueprint(pages)
    app.register_blueprint(auth)
    app.register_blueprint(api)

    register_pages(app)
    return app

