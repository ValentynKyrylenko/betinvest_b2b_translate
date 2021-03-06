# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-29 14:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_topic_owner'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='topic',
            managers=[
                ('managers', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='text',
            new_name='event',
        ),
        migrations.AddField(
            model_name='topic',
            name='asoc',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='topic',
            name='country',
            field=django_countries.fields.CountryField(default='', max_length=2),
        ),
        migrations.AddField(
            model_name='topic',
            name='devision',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='topic',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
        migrations.AddField(
            model_name='topic',
            name='league',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='topic',
            name='region',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='topic',
            name='sport',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='entry',
            name='text',
            field=models.URLField(blank=True, verbose_name='WWW'),
        ),
    ]
