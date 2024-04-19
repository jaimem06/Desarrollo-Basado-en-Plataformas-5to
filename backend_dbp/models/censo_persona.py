from app import db

class Censo_Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.String(60))
    lat = db.Column(db.Float)
    long = db.Column(db.Float)
    motivos = db.Column(db.String(250))
    # Relación muchos a uno con Persona y Censo
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'))
    censo_id = db.Column(db.Integer, db.ForeignKey('censo.id'))
    # Relación de uno a muchos con Motivo_Censo
    motivo_censo = db.relationship('Motivo_Censo', backref='censo_persona', lazy=True)