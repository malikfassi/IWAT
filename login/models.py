from django.db import models
from django.contrib.auth.models import User
from django import forms

class Utilisateur(models.Model):
	profilBase = models.OneToOneField(User, primary_key=True, related_name='profilBaseInUtilisateur')
	dateNaissance = models.DateField()
	#competences -> many-to-one-> utilisateur
    #historique(cours) -> many-to-one -> utilisateur
	#notification -> many-to-one -> utilisateur

	def __unicode__(self):
		return (self.profilBase.first_name+" "+self.profilBase.last_name+" @ "+self.profilBase.email)

	def __repr__(self):
		return self.__unicode__()

class UtilisateurForm(forms.Form):
	pseudo = forms.CharField(max_length=75)
	mdp = forms.CharField(max_length=75)