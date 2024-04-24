from app import db
import uuid
from models.rol import Rol

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    nombres = db.Column(db.String(100))
    apellidos = db.Column(db.String(100))
    estado = db.Column(db.Boolean, default=True)
    edad = db.Column(db.Integer)
    # Relación uno a muchos con Censo_Persona
    censos = db.relationship('Censo_Persona', backref='persona', lazy=True)
    id_rol = db.Column(db.Integer, db.ForeignKey('rol.id'), nullable = False)

    # Getters and setters
    @property
    def apellido(self):
        return self.apellidos

    @apellido.setter
    def apellido(self, value):
        self.apellidos = value

    @property
    def nombre(self):
        return self.nombres

    @nombre.setter
    def nombre(self, value):
        self.nombres = value
    
    def serialize(self):
        return {
            'external_id': self.external_id,
            'nombres': self.nombres,
            'apellidos': self.apellidos,
            'estado': self.estado,
            'edad': self.edad,
            'rol': self.rol.descripcion
        }
    # Mostrar el nombre del rol
    @property
    def rol_descripcion(self):
        return self.rol.descripcion if self.rol else None
   
#catalogo__motivo, censador, censo, censo__persona, motivo__censo, persona, rol