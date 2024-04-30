from app import db
import uuid
from datetime import datetime

class Censo (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    fecha_in = db.Column(db.Date)
    fecha_fin = db.Column(db.Date)
    motivo = db.Column(db.String(250))
    estado = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    # Relación uno a muchos con Censo_Persona
    censos = db.relationship('Censo_Persona', backref='censo', lazy=True)

    def serialize(self):
        return {
            'external_id': self.external_id,
            'fecha_in': self.fecha_in,
            'fecha_fin': self.fecha_fin,
            'motivo': self.motivo,
            'estado': 1 if self.estado else 0,
        }