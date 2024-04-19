from app import db
from models.tabla_asociacion import censadores_censos

class Censador (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.String(60))

    # Relación de muchos a muchos con Censo
    censos = db.relationship('Censo', secondary=censadores_censos, backref=db.backref('censadores', lazy=True))