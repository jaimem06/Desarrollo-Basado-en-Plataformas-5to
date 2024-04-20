from app import db
import uuid

class Motivo_Censo (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.VARVHAR(60), default=str(uuid.uud4()))