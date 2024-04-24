from app import db
import uuid

class Motivo (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.VARCHAR(100))
    estado = db.Column(db.Boolean, default=True)
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))