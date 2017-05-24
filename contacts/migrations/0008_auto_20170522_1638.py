# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 16:38
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_auto_20170522_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='product',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('SportsBook Live', 'SportsBook Live'), ('SportsBook Prematch', 'SportsBook Prematch'), ('WhiteLabel', 'WhiteLabel'), ('LandBased', 'LandBased')], max_length=56),
        ),
    ]