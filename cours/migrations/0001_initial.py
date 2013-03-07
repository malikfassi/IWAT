# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CourCompetence'
        db.create_table(u'cours_courcompetence', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('secteur', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('anneeSecteur', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'cours', ['CourCompetence'])

        # Adding model 'CourEvenement'
        db.create_table(u'cours_courevenement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sujet', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Cours(evenement)', to=orm['cours.CourCompetence'])),
            ('heure', self.gf('django.db.models.fields.DateTimeField')()),
            ('lieu', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('eleve', self.gf('django.db.models.fields.related.ForeignKey')(related_name='eleve-in-Cour', to=orm['login.Utilisateur'])),
            ('prof', self.gf('django.db.models.fields.related.ForeignKey')(related_name='prof-in-Cour', to=orm['login.Utilisateur'])),
        ))
        db.send_create_signal(u'cours', ['CourEvenement'])

        # Adding model 'CourCompetenceUser'
        db.create_table(u'cours_courcompetenceuser', (
            ('utilisateurCompetent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='CourCompetenceUser-cours', to=orm['login.Utilisateur'])),
            ('competence', self.gf('django.db.models.fields.related.OneToOneField')(related_name='CompetenceInCourCompetenceUser', unique=True, primary_key=True, to=orm['cours.CourCompetence'])),
        ))
        db.send_create_signal(u'cours', ['CourCompetenceUser'])


    def backwards(self, orm):
        # Deleting model 'CourCompetence'
        db.delete_table(u'cours_courcompetence')

        # Deleting model 'CourEvenement'
        db.delete_table(u'cours_courevenement')

        # Deleting model 'CourCompetenceUser'
        db.delete_table(u'cours_courcompetenceuser')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'cours.courcompetence': {
            'Meta': {'object_name': 'CourCompetence'},
            'anneeSecteur': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'secteur': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'cours.courcompetenceuser': {
            'Meta': {'object_name': 'CourCompetenceUser', '_ormbases': [u'cours.CourCompetence']},
            'competence': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CompetenceInCourCompetenceUser'", 'unique': 'True', 'primary_key': 'True', 'to': u"orm['cours.CourCompetence']"}),
            'utilisateurCompetent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'CourCompetenceUser-cours'", 'to': u"orm['login.Utilisateur']"})
        },
        u'cours.courevenement': {
            'Meta': {'object_name': 'CourEvenement'},
            'eleve': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'eleve-in-Cour'", 'to': u"orm['login.Utilisateur']"}),
            'heure': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lieu': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'prof': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'prof-in-Cour'", 'to': u"orm['login.Utilisateur']"}),
            'sujet': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Cours(evenement)'", 'to': u"orm['cours.CourCompetence']"})
        },
        u'login.utilisateur': {
            'Meta': {'object_name': 'Utilisateur'},
            'dateNaissance': ('django.db.models.fields.DateField', [], {}),
            'profilBase': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profilBaseInUtilisateur'", 'unique': 'True', 'primary_key': 'True', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['cours']