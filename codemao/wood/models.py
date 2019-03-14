from django.db import models

# Create your models here.


class Author(models.Model):
	name = models.CharField(max_length=20, null=False)


class Publisher(models.Model):
	name = models.CharField(max_length=30, null=False)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField(max_length=40)


class AuthorDetail(models.Model):
	sex = models.IntegerField(choices=((0, '男'), (1, '女')))
	email = models.EmailField(max_length=30)
	phone = models.CharField(max_length=20)
	age = models.IntegerField(null=False)
	author = models.OneToOneField(Author, on_delete=models.CASCADE)


class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
	publication_date = models.DateField()