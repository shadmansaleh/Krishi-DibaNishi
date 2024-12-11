from flask import Flask
from app.views import pages, register_pages
from app.api import api

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Register the Blueprint
    app.register_blueprint(pages)
    app.register_blueprint(api)

    register_pages(app)
    return app

