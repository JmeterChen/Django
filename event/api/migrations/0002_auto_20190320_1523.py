# Generated by Django 2.1.4 on 2019-03-20 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='times',
            field=models.DateTimeField(),
        ),
    ]