# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('sex', models.IntegerField(choices=[(1, b'\xe7\x94\xb7'), (2, b'\xe5\xa5\xb3')])),
                ('author', models.OneToOneField(to='index.Author')),
            ],
        ),
    ]
