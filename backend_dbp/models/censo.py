from app import db

class Censo (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.String(60))
    fecha_in = db.Column(db.Date)
    fecha_fin = db.Column(db.Date)
    motivo = db.Column(db.String(250))
    # Relación uno a muchos con Censo_Persona
    censo_persona = db.relationship('Censo_Persona', backref='censo', lazy=True)