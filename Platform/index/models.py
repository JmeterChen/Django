from django.db import models

# Create your models here.


class Student(models.Model):
	name = models.CharField(max_length=20, null=False)
	age = models.IntegerField(null=False)