from app import db

# Relacion de muchos a muchos de Censador y Censo
censadores_censos = db.Table('censadores_censos',
    db.Column('censador_id', db.Integer, db.ForeignKey('censador.id'), primary_key=True),
    db.Column('censo_id', db.Integer, db.ForeignKey('censo.id'), primary_key=True)
)