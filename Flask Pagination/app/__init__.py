from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
# ma = Marshmallow()

def create_app():
    global app
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
    app.config['SECRET_KEY'] = 'THIS is secret'

    from app.controllers import create_blueprint
    app.register_blueprint(create_blueprint())

    db.init_app(app)
    # ma.init_app(app)
    create_db()

    return app

def create_db():
    with app.app_context():
        db.create_all()