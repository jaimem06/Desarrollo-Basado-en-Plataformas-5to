from app import db
from models.rol import Rol
import uuid
from datetime import datetime

class Cuenta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(100))
    clave = db.Column(db.String(250))
    estado = db.Column(db.Boolean, default=True)
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id'), nullable = False)