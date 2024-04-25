from models.persona import Persona
from models.rol import Rol
from models.cuenta import Cuenta
import uuid
from app import db

class PersonaControl:

    # Metodo para listar personas
    def listar(self):
        return Persona.query.all()
    
    # Metodo para guardar persona
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

    # Metodo para guardar un censado    
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
    
    # Metodo para guardar un censador
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
        
    # Metodo para obtener una persona por external_id
    def obtener_por_external_id(self, external_id):
        return Persona.query.filter_by(external_id=external_id).first()
    
    # Metodo para modificar persona por external_id
    def modificar(self, external_id, data):
        persona = Persona.query.filter_by(external_id=external_id).first()
        if persona:
            persona.nombre = data.get('nombre', persona.nombre)
            persona.apellido = data.get('apellido', persona.apellido)
            persona.fecha_nac = data.get('fecha', persona.fecha_nac)
            persona.estado = data.get('estado', persona.estado)
            
            rol_nombre = data.get('rol')
            if rol_nombre:
                rol = Rol.query.filter_by(nombre=rol_nombre).first()
                if rol:
                    persona.id_rol = rol.id
            
            cuenta_data = data.get('cuenta')
            if cuenta_data:
                cuenta = Cuenta.query.filter_by(id_persona=persona.id).first()
                if cuenta:
                    cuenta.correo = cuenta_data.get('correo', cuenta.correo)
                    cuenta.clave = cuenta_data.get('clave', cuenta.clave)
            
            db.session.commit()
            return persona
        else:
            return None