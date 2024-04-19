from app import db

class Catalogo_Motivo (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.String(60))

    # Relación de muchos a uno con Motivo_Censo
    motivoCenso_id = db.Column(db.Integer, db.ForeignKey('motivo_censo.id'))