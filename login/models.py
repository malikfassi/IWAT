from django.db import models
from cours.models import ANNEE_ETUDE
from cours.models import MATIERES

class Utilisateur(models.Model):
	nom = models.CharField(max_length=30)
	prenom = models.Charfield(max_length = 30)
	dateNaissance = models.DateField()
	eMail = models.EmailField()
	annee = CharField(max_length = 2, choices = ANNEE_ETUDE)
	competence = CharField(max_length = 2, choices = MATIERES)
        #historique(cours) -> many-to-one -> utilisateur
	#reponseAnnonce -> many-to-one -> utilisateur
	
