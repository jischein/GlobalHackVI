# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shelters', '0004_shelter_place_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelter',
            name='place_id',
            field=models.CharField(max_length=40),
        ),
    ]
