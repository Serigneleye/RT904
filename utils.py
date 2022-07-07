from TP904.models import Candidat

def get_candidats():
    candidats = Candidat.query.all()
    return candidats
