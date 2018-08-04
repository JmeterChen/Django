#coding=utf-8

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20, null=False, unique=True)
    pwd = models.CharField(max_length=10, null=False)


class Author(models.Model):
    name = models.CharField(max_length=20, null=False)

class Detail(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=False)
    age = models.IntegerField(null=False)
    sex = models.IntegerField(choices=((1, '男'), (2, '女')))
    author = models.OneToOneField(Author)


class Publisher(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    address = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=20, null=False)


class Book(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    publisher = models.ForeignKey(Publisher)
    author = models.ManyToManyField(Author)


