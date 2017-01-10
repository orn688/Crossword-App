# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 04:44
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rows', models.IntegerField()),
                ('columns', models.IntegerField()),
                ('date_added', models.DateField()),
                ('difficulty', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=100)),
                ('data', models.FileField(upload_to='crossword/')),
                ('ans', models.CharField(default='', max_length=1000)),
                ('spots', models.CharField(default='', max_length=1000)),
                ('aClues', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1000), default=[], size=None)),
                ('dClues', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1000), default=[], size=None)),
                ('pdf', models.FileField(upload_to='pdf/')),
            ],
        ),
    ]