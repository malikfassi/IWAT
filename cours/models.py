# -*- coding: cp1252 -*-
from django.db import models
from login.models import Utilisateur
from django.forms import ModelForm

Matieres = (
        #Langues
        ('FR', 'Langue Francaise'),
        ('EN', 'Langue Anglaise'),
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

AnneeEtude = (
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

class CourCompetence(models.Model):
    secteur = models.CharField(max_length=2, choices=Matieres)
    anneeSecteur = models.CharField(max_length=2, choices=AnneeEtude)

    def __unicode__(self):
        return self.secteur+self.anneeSecteur

    def __repr__(self):
        return self.__unicode__()

class CourCompetenceForm(ModelForm):
    class Meta:
        model = CourCompetence


class CourEvenement(models.Model):
    sujet = models.ForeignKey(CourCompetence, related_name="Cours(evenement)")
    heure = models.DateTimeField()
    lieu = models.CharField(max_length=200)
    eleve = models.ForeignKey(Utilisateur, related_name="eleve-in-Cour")
    prof = models.ForeignKey(Utilisateur, related_name="prof-in-Cour")
    
    def __unicode__(self):
        #return("Cours de "+ self.secteur+" "+self.anneeSecteur)
        return("Eleve : "+self.eleve.__unicode__()+ " Professeur : " + self.prof.__unicode__() + " � " + self.lieu)

    def __repr__(self):
        return self.__unicode__()

class CourEvenementForm(ModelForm):
   sujet = CourCompetenceForm



class CourCompetenceUser(CourCompetence):            # |
    #courcompetenceuser -> many-to-one -> utilisateur  v
    utilisateurCompetent = models.ForeignKey(Utilisateur, related_name="CourCompetenceUser-cours")
    competence = models.OneToOneField(CourCompetence, related_name="CompetenceInCourCompetenceUser")
    def __unicode__(self):
        return self.CourCompetence.__unicode__() + " : " + self.utilisateurCompetent.__unicode__()

class CourCompetenceUserForm(ModelForm):
    class Meta:
        model = CourCompetenceUser

