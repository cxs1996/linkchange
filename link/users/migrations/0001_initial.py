# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-06-09 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_link', models.CharField(max_length=64)),
                ('short_link', models.CharField(max_length=64)),
            ],
        ),
    ]
