from models.persona import Persona
from models.rol import Rol
from models.cuenta import Cuenta
from controllers.utils.errors import Erros
import uuid
from app import db
import jwt
from datetime import datetime, timedelta, timezone
from flask import current_app
from models.tipoEstadoCivil import TipoEstadoCivil

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
    
    # Metodo para modificar una persona por id
    def modificar(self, external_id, data):
        # 1. Ob Persona
        persona = Persona.query.filter_by(external_id=external_id).first()

        # 2. Validar existe persona
        if persona:
            # 3. Actualizar atributos de persona
            persona.nombres = data.get('nombres', persona.nombres)
            persona.apellidos = data.get('apellidos', persona.apellidos)
            persona.fecha_nac = data.get('fecha_nac', persona.fecha_nac)
            persona.estado = data.get('estado', persona.estado)
            persona.id_rol = data.get('id_rol', persona.id_rol)

            # 4. Update
            db.session.commit()

            return persona
        else:
            # 5. Retornar -3 en caso de error
            return -3
        # Metodo para activar una cuenta
        
    def activar_cuenta(self, external_id):
        cuenta = Cuenta.query.filter_by(external_id=external_id).first()
        if cuenta:
            cuenta.estado = True
            db.session.commit()
            return cuenta
        else:
            return None
    
    # Metodo para desactivar una cuenta
    def desactivar_cuenta(self, external_id):
        cuenta = Cuenta.query.filter_by(external_id=external_id).first()
        if cuenta:
            cuenta.estado = False
            db.session.commit()
            return cuenta
        else:
            return None
        
    def inicio_sesion(self, data):
        cuentaA = Cuenta.query.filter_by(correo = data.get('correo')).first()
        if cuentaA:
            # TODO encriptar
            if cuentaA.clave == data["clave"]:
                token = jwt.encode(
                    {
                        "external": cuentaA.external_id,
                        "expiracion": (datetime.now(timezone.utc) + timedelta(minutes=60)).isoformat()
                    }, 
                    key = current_app.config["SECRET_KEY"],
                    algorithm="HS512"
                )
                cuenta = Cuenta()
                cuenta.copy(cuentaA)
                persona = cuentaA.getPersona(cuentaA.id_persona)
                info = {
                    "token": token,
                    "user": persona.apellidos + " " + persona.nombres
                }
                return info
            else:
                return -5
        else:
            return -5
    
    def listar_estados_civiles(self):
        return [estado.name for estado in TipoEstadoCivil]
    