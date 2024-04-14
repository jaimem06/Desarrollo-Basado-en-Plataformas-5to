from app import db

class Practicando(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    edad = db.Column(db.Integer)
    cumpleaños = db.Column(db.Date)
