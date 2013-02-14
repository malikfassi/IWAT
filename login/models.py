from django.db import models

# Create your models here.

class Utilisateur(models.Models):
	nom = models.CharField(max_length=30)
	prenom = models.Charfield(max_length = 30)
	dateNaissance = models.DateField()
	eMail = models.EmailField()
	histoCours = models.ForeignKey('cours.cour')
	