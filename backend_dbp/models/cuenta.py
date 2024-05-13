from app import db
import uuid
from datetime import datetime

class Cuenta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(100))
    clave = db.Column(db.String(250))
    estado = db.Column(db.Boolean, default=True)
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id'), nullable = False)
    #persona = db.relationship('Persona', backref='cuenta', lazy=True)

    def getPersona(self, id_p):
        from models.persona import Persona
        return Persona.query.filter_by(id = id_p).first()

    def copy(self, value):
        self.correo = value.correo
        self.clave = value.clave
        self.estado = value.estado
        self.id = value.id
        self.external_id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        return self