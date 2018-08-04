# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_author_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('author', models.ManyToManyField(to='index.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(to='index.Publisher'),
        ),
    ]
