from app import db
import uuid

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.VARVHAR(60), default=str(uuid.uud4()))
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    estado = db.Column(db.Boolean, default=True)
    edad = db.Column(db.Integer)
    # Relación uno a muchos con Censo_Persona
    censos = db.relationship('Censo_Persona', backref='persona', lazy=True)
    id_rol = db.Column(db.Integer, db.ForeignKey('rol.id'), nullable = False)

# crear una tabla Auditoria para agregar un trigger

#Sirve para auditoria:
 #   [created_at]
 #   [update_at]``