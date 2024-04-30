from app import db
import uuid
from datetime import datetime

class Censo_Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    lat = db.Column(db.Float)
    long = db.Column(db.Float)
    motivo = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    # Relación muchos a uno con Persona
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'))
    # Relación muchos a uno con Censo
    censo_id = db.Column(db.Integer, db.ForeignKey('censo.id'))