# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-30 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctcapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='submitted',
            field=models.DateField(null=True),
        ),
    ]
