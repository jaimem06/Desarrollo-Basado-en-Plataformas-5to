from app import db

class Motivo_Censo (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.String(60))

    # Relación de muchos a uno con Censo_Persona
    censoPersona_id = db.Column(db.Integer, db.ForeignKey('censo_persona.id'))
    # Relación de uno a muchos con Catalogo_Motivo
    catalogoMotivo = db.relationship('Catalogo_Motivo', backref='censo_persona', lazy=True)