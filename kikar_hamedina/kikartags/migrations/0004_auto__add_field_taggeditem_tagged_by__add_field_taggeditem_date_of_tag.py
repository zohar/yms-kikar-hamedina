# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TaggedItem.tagged_by'
        db.add_column(u'kikartags_taggeditem', 'tagged_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='tagged', null=True, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'TaggedItem.date_of_tagging'
        db.add_column(u'kikartags_taggeditem', 'date_of_tagging',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 10, 18, 0, 0), null=True),
                      keep_default=False)

        # Adding unique constraint on 'TagSynonym', fields ['tag', 'synonym_tag']
        db.create_unique(u'kikartags_tagsynonym', ['tag_id', 'synonym_tag_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'TagSynonym', fields ['tag', 'synonym_tag']
        db.delete_unique(u'kikartags_tagsynonym', ['tag_id', 'synonym_tag_id'])

        # Deleting field 'TaggedItem.tagged_by'
        db.delete_column(u'kikartags_taggeditem', 'tagged_by_id')

        # Deleting field 'TaggedItem.date_of_tagging'
        db.delete_column(u'kikartags_taggeditem', 'date_of_tagging')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'kikartags.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_for_main_display': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'kikartags.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'kikartags_taggeditem_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            'date_of_tagging': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 10, 18, 0, 0)', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'kikartags_taggeditem_items'", 'to': u"orm['kikartags.Tag']"}),
            'tagged_by': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'tagged'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'kikartags.tagsynonym': {
            'Meta': {'unique_together': "(('tag', 'synonym_tag'),)", 'object_name': 'TagSynonym'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'synonym_tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'synonym_synonym_tag'", 'unique': 'True', 'to': u"orm['kikartags.Tag']"}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'synonym_proper_tag'", 'to': u"orm['kikartags.Tag']"})
        }
    }

    complete_apps = ['kikartags']