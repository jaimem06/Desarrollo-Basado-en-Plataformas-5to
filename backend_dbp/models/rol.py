from app import db
import uuid

class Rol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.String(100))
    estado = db.Column(db.Boolean, default=True)
    external_id = db.Column(db.VARVHAR(60), default=str(uuid.uud4()))
    
    # 1 rol tiene muchas personas
    roles = db.relationship('Persona', backref='rol', lazy=True)