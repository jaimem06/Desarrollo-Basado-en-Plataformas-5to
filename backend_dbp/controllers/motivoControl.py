import uuid
from app import db
from models.motivo import Motivo
from tokenizer import split_into_sentences

class MotivoControl:
    def listar(self):
        return Motivo.query.all()
    
    def listar_activos(self):
        return Motivo.query.filter_by(estado=True).all()

    # Tokenizar
    def save_str(self, text):
        g = split_into_sentences(text)
        tokens = []
        for sentence in g:
            print(sentence)
            tokens = sentence.split()
        print(tokens)
        # Guardar en la base
        if len(tokens) > 0:
            for m in tokens:
                motivo = Motivo()
                motivo.nombre = m
                motivo.estado = True
                motivo.external_id = str(uuid.uuid4())
                db.session.add(motivo)
                db.session.commit()
            return 0
        else:
            return -3
    
    # Activar motivo
    def activar(self, external_id):
        motivo = Motivo.query.filter_by(external_id=external_id).first()
        if motivo:
            motivo.estado = True
            db.session.commit()
            return 0
        else:
            return -3
    
    # Desactivar motivo
    def desactivar(self, external_id):
        motivo = Motivo.query.filter_by(external_id=external_id).first()
        if motivo:
            motivo.estado = False
            db.session.commit()
            return 0
        else:
            return -3