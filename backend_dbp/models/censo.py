from app import db
import uuid

class Censo (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.VARVHAR(60), default=str(uuid.uud4()))
    fecha_in = db.Column(db.Date)
    fecha_fin = db.Column(db.Date)
    motivo = db.Column(db.String(250))