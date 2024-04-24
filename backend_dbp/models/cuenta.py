from app import db
from models.rol import Rol
import uuid

class Cuenta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(100))
    clave = db.Column(db.String(100))
    estado = db.Column(db.Boolean, default=True)
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id'))

    # Relación uno a uno con Persona
    persona = db.relationship('Persona', backref='cuenta', uselist=False)