from django.db import models
from cours.models import CourEvenement
from login.models import Utilisateur
from django.forms import ModelForm

class Annonce(models.Model):
    contexte = models.OneToOneField(CourEvenement, related_name="contexteInAnnonce")
    posterPar = models.OneToOneField(Utilisateur, related_name="posteurInAnnonce")

    def __unicode__(self):
        return (self.posterPar.__unicode__()+ " cherche un cour de " + self.contexte.__unicode__())

    def __repr__(self):
        return self.__unicode__()

class AnnonceForm(ModelForm):
    class Meta:
        model = Annonce
 
class Notification(models.Model):
    emetteur = models.ForeignKey(Utilisateur, related_name="emetteurInNotification")
    recepteur = models.ForeignKey(Utilisateur, related_name="recepteurInNotification")
    message = models.CharField(max_length=750)
    vu = models.BooleanField()

    def __unicode__(self):
        return self.message

    def __repr__(self):
        return self.__unicode__()