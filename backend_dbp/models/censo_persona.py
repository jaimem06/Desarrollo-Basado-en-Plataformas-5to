from app import db

class Censo_Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.String(60))
    lat = db.Column(db.Float)
    long = db.Column(db.Float)
    motivos = db.Column(db.String(250))
    # Relación muchos a uno con Persona
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'))