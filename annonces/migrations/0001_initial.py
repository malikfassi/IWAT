# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Annonce'
        db.create_table(u'annonces_annonce', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contexte', self.gf('django.db.models.fields.related.OneToOneField')(related_name='contexteInAnnonce', unique=True, to=orm['cours.CourEvenement'])),
            ('posterPar', self.gf('django.db.models.fields.related.OneToOneField')(related_name='posteurInAnnonce', unique=True, to=orm['login.Utilisateur'])),
        ))
        db.send_create_signal(u'annonces', ['Annonce'])

        # Adding model 'Notification'
        db.create_table(u'annonces_notification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('emetteur', self.gf('django.db.models.fields.related.ForeignKey')(related_name='emetteurInNotification', to=orm['login.Utilisateur'])),
            ('recepteur', self.gf('django.db.models.fields.related.ForeignKey')(related_name='recepteurInNotification', to=orm['login.Utilisateur'])),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=750)),
            ('vu', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'annonces', ['Notification'])


    def backwards(self, orm):
        # Deleting model 'Annonce'
        db.delete_table(u'annonces_annonce')

        # Deleting model 'Notification'
        db.delete_table(u'annonces_notification')


    models = {
        u'annonces.annonce': {
            'Meta': {'object_name': 'Annonce'},
            'contexte': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'contexteInAnnonce'", 'unique': 'True', 'to': u"orm['cours.CourEvenement']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posterPar': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'posteurInAnnonce'", 'unique': 'True', 'to': u"orm['login.Utilisateur']"})
        },
        u'annonces.notification': {
            'Meta': {'object_name': 'Notification'},
            'emetteur': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'emetteurInNotification'", 'to': u"orm['login.Utilisateur']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '750'}),
            'recepteur': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'recepteurInNotification'", 'to': u"orm['login.Utilisateur']"}),
            'vu': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
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

    complete_apps = ['annonces']