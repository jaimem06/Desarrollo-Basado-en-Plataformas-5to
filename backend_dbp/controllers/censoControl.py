from models.censo import Censo
from models.censo_persona import Censo_Persona
from models.motivo import Motivo
from controllers.utils.errors import Erros

import uuid
from app import db

class CensoControl:

    # Metodo para listar censos
    def listar(self):
        return Censo.query.all()
    
    # Metodo para guardar censo
    def guardar(self, data):
        censo = Censo()
        censo.fecha_in = data.get('fecha_in')
        censo.fecha_fin = data.get('fecha_fin')
        censo.motivo = data.get('motivo')
        censo.estado = data.get('estado')
        db.session.add(censo)
        db.session.commit()
        return censo.id

    # Metodo para obtener un censo por external_id
    def obtener_por_external_id(self, external_id):
        return Censo.query.filter_by(external_id=external_id).first()
    
    # Metodo para modificar un censo por id
    def modificar(self, external_id, data):
        censo = Censo.query.filter_by(external_id=external_id).first()
        if censo:
            censo.fecha_in = data.get('fecha_in', censo.fecha_in)
            censo.fecha_fin = data.get('fecha_fin', censo.fecha_fin)
            censo.motivo = data.get('motivo', censo.motivo)
            censo.estado = data.get('estado', censo.estado)
            db.session.commit()
            return censo
        else:
            return None
    
    # Metodo para activar un censo
    def activar_censo(self, external_id):
        censo = Censo.query.filter_by(external_id=external_id).first()
        if censo:
            censo.estado = True
            db.session.commit()
            return censo
        else:
            return None

    # Metodo para desactivar un censo
    def desactivar_censo(self, external_id):
        censo = Censo.query.filter_by(external_id=external_id).first()
        if censo:
            censo.estado = False
            db.session.commit()
            return censo
        else:
            return None

    # Metodo para guardar censo_persona
    def guardar_datos_censo(self, data):
        censo_persona = Censo_Persona()
        censo_persona.lat = data.get('lat')
        censo_persona.long = data.get('long')

        # Buscar motivos por nombre
        motivo_nombres = [nombre.strip() for nombre in data.get('motivo').split(',')]
        motivos = Motivo.query.filter(Motivo.nombre.in_(motivo_nombres)).all()
        if motivos:
            censo_persona.motivo = ', '.join(motivo.nombre for motivo in motivos)
        else:
            return -4

        db.session.add(censo_persona)
        db.session.commit()
        return censo_persona.id