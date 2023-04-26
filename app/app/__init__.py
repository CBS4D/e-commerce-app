from flask import Flask

from models import db
from schemas import ma
from api import app_api

flask_app = Flask(__name__)
app_api.init_app(flask_app)


def create_app(config):
    """
    App Factory function, binds all the extensions and resources
    and returns an application object
    """
    flask_app.config.from_object(config)

    db.init_app(flask_app)
    ma.init_app(flask_app)

    with flask_app.app_context():
        db.create_all()

    return flask_app
