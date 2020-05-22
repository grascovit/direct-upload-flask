import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

from direct_upload.api import api
from direct_upload.db import db, migrate
from direct_upload.models import *

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    CORS(app)

    from direct_upload.views import blueprint, document_blueprint

    app.register_blueprint(blueprint)
    app.register_blueprint(document_blueprint)

    return app
