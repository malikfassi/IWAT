# -*- coding: cp1252 -*-
from django.db import models
from profil import Eleve, Professeur

MATIERES = (
        #Langues
        ('FR', 'Langue Francaise'),
        ('En', 'Langue Anglaise'),
        ('NL', 'Langue Néerlandaise'),
        #sciences
        ('SM', 'Science des Mathématiques'),
        ('SB', 'Science de la biologie'),
        ('SP', 'Science de la physique'),
        ('SC', 'Science de la chimie'),
        ('SG', 'Science humaine (géographie)'),
        ('SH', 'Science humaine (histoire)'),
        ('SP', 'Science humaine (philosophie)'),
        #litérature
        ('LF', 'Littérature Francaise'),
        ('LA', 'Littérature Anglaise'),
        ('LN', 'Littérature Néerlandaise'),
        #autres
        ('EC', 'Economie'),
        ('MO', 'Morale'),
        ('RE', 'Religion'),
    )

ANNEE_ETUDE = (
        #primaire
        ('P1', '1ére primaire'),
        ('P2', '2ére primaire'),
        ('P3', '3ére primaire'),
        ('P4', '4ére primaire'),
        ('P5', '5ére primaire'),
        ('P6', '6ére primaire'),
        #secondaire
        ('S1', '1ére secondaire'),
        ('S2', '2ére secondaire'),
        ('S3', '3ére secondaire'),
        ('S4', '4ére secondaire'),
        ('S5', '5ére secondaire'),
        ('S6', '6ére secondaire'),
        #supérieur
        ('B1', 'Bachelier 1ére'),
        ('B3', 'Bachelier 3ére'),
        ('B2', 'Bachelier 2ére'),
        ('M1', 'Master 1ére'),
        ('M2', 'Master 2ére'),
    )

class Cour(models.Models):
    secteur = models.CharField(max_length=2, choices=MATIERES)
    anneeSecteur = models.CharField(max_length=2, choices=ANNEE_ETUDE)
    heure = models.DateField()
    lieu = CharField(max_length=200)
    eleve = ForeignKey('profil.Eleve')
    prof = ForeignKey('profil.Professeur')
    
    def __unicode__(self):
        return("Eleve : "+eleve.__unicode__()+ " Professeur : " prof.__unicode__() + " Le " + heure + " à " + lieu)
