# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-16 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artiste', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('date_released', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'music category',
                'verbose_name_plural': 'music category',
                'ordering': ['artiste'],
            },
        ),
    ]
