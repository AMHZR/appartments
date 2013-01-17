# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'localities'
        db.create_table('property_localities', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('property', ['localities'])

        # Adding model 'parking'
        db.create_table('property_parking', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('how_many', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('property', ['parking'])

        # Adding model 'amenities'
        db.create_table('property_amenities', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('property', ['amenities'])

        # Adding model 'contacts'
        db.create_table('property_contacts', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('contact_person', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('phone_office', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('facebook', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('twitter', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('office_hours', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('property', ['contacts'])

        # Adding model 'projects'
        db.create_table('property_projects', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('floor_plans', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('min_bathrooms', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('max_bathrooms', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('min_price', self.gf('django.db.models.fields.IntegerField')()),
            ('max_price', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('contacts', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.contacts'])),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('started_on', self.gf('django.db.models.fields.DateField')()),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('property', ['projects'])

        # Adding M2M table for field amenities on 'projects'
        m2m_table_name = db.shorten_name('property_projects_amenities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('projects', models.ForeignKey(orm['property.projects'], null=False)),
            ('amenities', models.ForeignKey(orm['property.amenities'], null=False))
        ))
        db.create_unique(m2m_table_name, ['projects_id', 'amenities_id'])

        # Adding model 'property'
        db.create_table('property_property', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('available_from', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('sale_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('constructed_on', self.gf('django.db.models.fields.DateField')()),
            ('project_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.projects'])),
            ('locality', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.localities'])),
            ('bath_no', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('room_no', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('built_up_area', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('carpet_area', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('on_floor', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('balconies', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('parking', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.parking'])),
            ('parking_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('direction_facing', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('flooring', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('owner_ship', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('negotiable', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
            ('credit_score', self.gf('django.db.models.fields.FloatField')()),
            ('posted_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('property', ['property'])


    def backwards(self, orm):
        # Deleting model 'localities'
        db.delete_table('property_localities')

        # Deleting model 'parking'
        db.delete_table('property_parking')

        # Deleting model 'amenities'
        db.delete_table('property_amenities')

        # Deleting model 'contacts'
        db.delete_table('property_contacts')

        # Deleting model 'projects'
        db.delete_table('property_projects')

        # Removing M2M table for field amenities on 'projects'
        db.delete_table(db.shorten_name('property_projects_amenities'))

        # Deleting model 'property'
        db.delete_table('property_property')


    models = {
        'property.amenities': {
            'Meta': {'object_name': 'amenities'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'property.contacts': {
            'Meta': {'object_name': 'contacts'},
            'contact_person': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'office_hours': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone_office': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'property.localities': {
            'Meta': {'object_name': 'localities'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'property.parking': {
            'Meta': {'object_name': 'parking'},
            'how_many': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'property.projects': {
            'Meta': {'object_name': 'projects'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'amenities': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['property.amenities']", 'symmetrical': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'contacts': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['property.contacts']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'floor_plans': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_bathrooms': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'max_price': ('django.db.models.fields.IntegerField', [], {}),
            'min_bathrooms': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'min_price': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'started_on': ('django.db.models.fields.DateField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'property.property': {
            'Meta': {'object_name': 'property'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'available_from': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'balconies': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bath_no': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'built_up_area': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'carpet_area': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'constructed_on': ('django.db.models.fields.DateField', [], {}),
            'credit_score': ('django.db.models.fields.FloatField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'direction_facing': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'flooring': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locality': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['property.localities']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'negotiable': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'on_floor': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'owner_ship': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parking': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['property.parking']"}),
            'parking_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'posted_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'project_name': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['property.projects']"}),
            'room_no': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'sale_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'value': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['property']