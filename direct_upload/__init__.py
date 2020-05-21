import os

from dotenv import load_dotenv
from flask import Flask

from direct_upload.api import api
from direct_upload.db import db, migrate
from direct_upload.models import *

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    return app
