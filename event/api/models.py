from django.db import models

# Create your models here.


class Event(models.Model):
	title = models.CharField(max_length=30, null=False, unique=True)
	limit = models.IntegerField(default=200, null=False)
	status = models.IntegerField(choices=((0, '未开始'), (1, '进行中'), (2, '已结束')), default=0)
	addres = models.CharField(max_length=50, null=False)
	times = models.DateField(null=False)
	
	
class Guess(models.Model):
	name = models.CharField(max_length=20, null=False)
	phone_number = models.CharField(max_length=15, null=False, unique=True)
	e_mail = models.EmailField(max_length=30, null=True, unique=True)
	event = models.ManyToManyField(Event)