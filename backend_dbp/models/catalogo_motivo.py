from app import db
import uuid

class Catalogo_Motivo (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    nombre = db.Column(db.String(100))
    estado = db.Column(db.Boolean, default=True)