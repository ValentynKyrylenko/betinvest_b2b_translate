# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-25 07:15
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0011_auto_20170524_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='product',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('SportsBook Live', 'SportsBook Live'), ('SportsBook Prematch', 'SportsBook Prematch'), ('WhiteLabel', 'WhiteLabel'), ('LandBased', 'LandBased'), ('Other', 'Other')], max_length=62),
        ),
        migrations.AlterField(
            model_name='customer',
            name='website',
            field=models.URLField(blank=True, verbose_name='WWW'),
        ),
    ]
