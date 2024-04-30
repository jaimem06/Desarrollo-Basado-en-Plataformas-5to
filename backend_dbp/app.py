from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()
import MySQLdb
#import config.config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    #TODO
    app.config.from_object('config.config.Config')
    db.init_app(app)

    with app.app_context():
        from routes. api import api
        from routes. api_persona import api_persona
        from routes. api_censo import api_censo
        from routes. api_motivo import api_motivo
        app.register_blueprint(api)
        app.register_blueprint(api_persona)
        app.register_blueprint(api_censo)
        app.register_blueprint(api_motivo)
        # Creacion de tablas en la base de datos
        db.create_all()
        #db.drop_all()
    return app
