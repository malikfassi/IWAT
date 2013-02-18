from django.db import models
from cours.models import ANNEE_ETUDE
from cours.models import MATIERES
from login.models import utilisateur

class Annonce(models.Model):
    posterPar = models.ForeignKey(Utilisateur)
    secteur = models.CharField(max_length = 2, choices = MATIERES)
    anneeSecteur = models.CharField(max_length = 2, choices = ANNEE_ETUDE)
    lieu = models.CharField(max_length = 200)
    date = models.DateField()

    def __unicode__(self):
        return (self.posterPar.__unicode__()+ " cherche un cour de " + self.secteur)
    
class ReponsseAnnonce(models.Model):
    annonceConcernee = models.ForeignKey(Annonce)
    profRepondant = models.ForeignKey(Utilisateur)
    messagePerso = CharField(max_length=250)
    vu = models.BooleanField()
    prix = DecimalFieldField(max_digits=4, decimal_places=2)
    
    
