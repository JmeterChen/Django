from django.db import models

# Create your models here.


class Students(models.Model):
    name = models.CharField(max_length=10, null=False)
    age = models.IntegerField(null=False)
    

class Users(models.Model):
    username = models.CharField(max_length=10, null=False, unique=True)
    password = models.CharField(max_length=10, null=False)
    email = models.EmailField(max_length=20, null=False)
