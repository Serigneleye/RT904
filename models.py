from flask_sqlalchemy import SQLAlchemy
from .views import app 
import logging as lg
# Create database connection object
db = SQLAlchemy(app)

class Candidat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prenom = db.Column(db.String(200), nullable=False)
    nom = db.Column(db.String(200), nullable=False)
    votes = db.Column(db.Integer(), nullable=False)

    def __init__(self, prenom, nom, votes):
        self.prenom = prenom
        self.nom = nom
        self.votes = votes

db.create_all()
def init_db():
        db.drop_all()
        db.create_all()
        db.session.add(Candidat("Serigne","LEYE",0))
        db.session.add(Candidat("Ababacar","DIBA",0))
        db.session.add(Candidat("Moustapha","DIOP",0))
        db.session.add(Candidat("Soda","KANE",0))
        db.session.commit()
        lg.warning('Database Initialized!')

