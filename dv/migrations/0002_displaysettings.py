# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisplaySettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
                ('quarter', models.CharField(max_length=200)),
                ('month', models.CharField(max_length=200)),
            ],
        ),
    ]