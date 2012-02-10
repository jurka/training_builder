# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Program.for_women'
        db.add_column('builder_program', 'for_women', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Exercise.for_women'
        db.add_column('builder_exercise', 'for_women', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Program.for_women'
        db.delete_column('builder_program', 'for_women')

        # Deleting field 'Exercise.for_women'
        db.delete_column('builder_exercise', 'for_women')


    models = {
        'builder.day': {
            'Meta': {'object_name': 'Day'},
            'day_number': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pr_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['builder.Program']"}),
            'week_number': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'builder.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'for_women': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_link': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'link_to': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'video_link': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'builder.program': {
            'Meta': {'object_name': 'Program'},
            'for_women': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'builder.task': {
            'Meta': {'object_name': 'Task'},
            'day_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['builder.Day']"}),
            'excercise_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['builder.Exercise']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_light_weight': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'reps': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'super_set_number': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['builder']
