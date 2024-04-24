from models.persona import Persona
from models.rol import Rol
from models.cuenta import Cuenta
import uuid
from app import db

# [a-zA-Z0-9_]+([.][a-zA-Z0-9_]+)*@[a-zA-Z0-9_]+([.][a-zA-Z0-9_]+)*[.][a-zA-Z]{2,5}

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
        
    def guardar_censado(self, data):
        rol = Rol.query.filter_by(nombre="CENSADO").first()
        persona = Persona()
        if rol:
            persona.external_id = str(uuid.uuid4())
            persona.nombre = data.get('nombres')
            persona.apellido = data.get('apellidos')
            persona.estado = data.get('estado')
            persona.fecha_nac = data.get('fecha_nac')
            persona.id_rol = rol.id
            db.session.add(persona)
            db.session.commit()
            return persona.id
        else:
            return -1
        
    def guardar_censador(self, data):
        persona = Persona()
        rol = Rol.query.filter_by(nombre="CENSADOR").first()
        if rol:
            cuenta = Cuenta.query.filter_by(correo = data.get('correo')).first()
            if cuenta:
                return -2
            else:
                # Persona
                persona.external_id = str(uuid.uuid4())
                persona.nombre = data.get('nombres')
                persona.apellido = data.get('apellidos')
                persona.estado = data.get('estado')
                persona.fecha_nac = data.get('fecha_nac')
                persona.id_rol = rol.id
                db.session.add(persona)
                db.session.commit()
                # Cuenta
                cuenta_new = Cuenta()
                cuenta_new.correo = data.get('correo')
                cuenta_new.clave = data.get('clave')
                cuenta_new.external_id = str(uuid.uuid4())
                cuenta_new.id_persona = persona.id
                db.session.add(cuenta_new)
                db.session.commit()
                return cuenta_new.id
        else:
            return -1