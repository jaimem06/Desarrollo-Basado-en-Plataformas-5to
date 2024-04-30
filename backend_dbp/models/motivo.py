from app import db
import uuid
from datetime import datetime

class Motivo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    estado = db.Column(db.Boolean, default=True)
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def serialize(self):
        return {
            'external_id': self.external_id,
            'nombre': self.nombre,
            'estado': 1 if self.estado else 0,
        }