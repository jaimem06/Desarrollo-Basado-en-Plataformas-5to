from app import db
import uuid

class Censo_Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.VARVHAR(60), default=str(uuid.uud4()))
    lat = db.Column(db.Float)
    long = db.Column(db.Float)
    motivos = db.Column(db.String(250))
    # Relación muchos a uno con Persona
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'))