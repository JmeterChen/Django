from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20, null=False, unique=True)
    email = models.EmailField(max_length=50, null=False, unique=True)
    password = models.CharField(max_length=32, null=False)


class Task(models.Model):
    name = models.CharField(max_length=20, null=False, unique=True)
    desc = models.CharField(max_length=50)

