from models.persona import Persona
import uuid
from app import db

class PersonaControl:
    def listar(self):
        return Persona.query.all()
    
    def guardar(self, data):
        persona = Persona()
        persona.apellido = data.get('apellidos')
        persona.nombre = data.get('nombres')
        persona.fechanac = data.get('fecha')
        persona.external_id = uuid.uuid4()
        persona.estado = data.get('estado')
        db.session.add(persona)
        db.session.commit()
        return persona.id
        
    def crear (self, data):
        persona = Persona()
        persona.external_id = str(uuid.uuid4())
        persona.nombres = data.get('nombres')
        persona.apellidos = data.get('apellidos')
        persona.estado = data.get('estado')
        persona.edad = data.get('edad')
        persona.id_rol = data.get('id_rol')
        db.session.add(persona)
        db.session.commit()
        return persona