# -*- coding: cp1252 -*-
from django.db import models
from login.models import Utilisateur

MATIERES = (
        #Langues
        ('FR', 'Langue Francaise'),
        ('En', 'Langue Anglaise'),
        ('NL', 'Langue N�erlandaise'),
        #sciences
        ('SM', 'Science des Math�matiques'),
        ('SB', 'Science de la biologie'),
        ('SP', 'Science de la physique'),
        ('SC', 'Science de la chimie'),
        ('SG', 'Science humaine (g�ographie)'),
        ('SH', 'Science humaine (histoire)'),
        ('SP', 'Science humaine (philosophie)'),
        #lit�rature
        ('LF', 'Litt�rature Francaise'),
        ('LA', 'Litt�rature Anglaise'),
        ('LN', 'Litt�rature N�erlandaise'),
        #autres
        ('EC', 'Economie'),
        ('MO', 'Morale'),
        ('RE', 'Religion'),
    )

ANNEE_ETUDE = (
        #primaire
        ('P1', '1�re primaire'),
        ('P2', '2�re primaire'),
        ('P3', '3�re primaire'),
        ('P4', '4�re primaire'),
        ('P5', '5�re primaire'),
        ('P6', '6�re primaire'),
        #secondaire
        ('S1', '1�re secondaire'),
        ('S2', '2�re secondaire'),
        ('S3', '3�re secondaire'),
        ('S4', '4�re secondaire'),
        ('S5', '5�re secondaire'),
        ('S6', '6�re secondaire'),
        #sup�rieur
        ('B1', 'Bachelier 1�re'),
        ('B3', 'Bachelier 3�re'),
        ('B2', 'Bachelier 2�re'),
        ('M1', 'Master 1�re'),
        ('M2', 'Master 2�re'),
    )

class Cour(models.Model):
    secteur = models.CharField(max_length=2, choices=MATIERES)
    anneeSecteur = models.CharField(max_length=2, choices=ANNEE_ETUDE)
    heure = models.DateTimeField()
    lieu = models.CharField(max_length=200)
    eleve = ForeignKey(Utilisateur)
    prof = ForeignKey(Utilisateur)
    
    def __unicode__(self):
        #return("Cours de "+ self.secteur+" "+self.anneeSecteur)
        return("Eleve : "+eleve.__unicode__()+ " Professeur : " + prof.__unicode__() + " Le " + heure + " � " + lieu)
