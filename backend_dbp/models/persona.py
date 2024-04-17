from app import db

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.String(60))
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    estado = db.Column(db.Boolean, default=True)
    edad = db.Column(db.Integer)
    # Relación uno a muchos con Censo_Persona
    censos = db.relationship('Censo_Persona', backref='persona', lazy=True)
