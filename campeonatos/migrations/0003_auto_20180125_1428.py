# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-25 16:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campeonatos', '0002_auto_20180125_1145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='edicoe',
            old_name='campeonato_id',
            new_name='julinha',
        ),
    ]