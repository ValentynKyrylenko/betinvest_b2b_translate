# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20170513_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='business_type',
            field=models.CharField(max_length=80, verbose_name='Type of the contact'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='company_name',
            field=models.CharField(blank=True, max_length=80, verbose_name='Legal Company name'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='contacted_on',
            field=models.DateField(blank=True, null=True, verbose_name='Date of last contact'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='country',
            field=models.CharField(max_length=80, verbose_name='Country of registering'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail address'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='exibition',
            field=models.CharField(blank=True, max_length=50, verbose_name='Met on...'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='person_name',
            field=models.CharField(max_length=80, verbose_name='Name and Surname of the Person'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='website',
            field=models.URLField(blank=True, verbose_name='Official WWW'),
        ),
    ]
