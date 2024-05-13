from app import db
import uuid
from datetime import datetime
from models.tipoEstadoCivil import TipoEstadoCivil

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    nombres = db.Column(db.String(100))
    apellidos = db.Column(db.String(100))
    estado = db.Column(db.Enum(TipoEstadoCivil))
    fecha_nac = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    # Relación uno a muchos con Censo_Persona
    censos = db.relationship('Censo_Persona', backref='persona', lazy=True)
    id_rol = db.Column(db.Integer, db.ForeignKey('rol.id'), nullable = False)
    cuenta = db.relationship('Cuenta', backref='persona', lazy=True)

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
            'estado': self.estado.serialize() if self.estado else None,
            'fecha_nac': self.fecha_nac.isoformat() if self.fecha_nac else None,
        }
    
    def copy(self):
        new_persona = Persona(
            id=self.id,
            nombres=self.nombres,
            apellidos=self.apellidos,
            fecha_nac=self.fecha_nac,
            estado=self.estado,
            external_id=self.external_id,
            id_rol =self.id_rol
            # Añade otros atributos aquí si es necesario
        )
        return new_persona
        
#catalogo__motivo, censador, censo, censo__persona, motivo__censo, persona, rol, motivo