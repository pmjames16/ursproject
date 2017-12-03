from django.db import models
#from django.utils import timezone


class Place(models.Model):
	id = models.PositiveIntegerField(primary_key=True)
	name = models.CharField(max_length = 200)
	camp = models.CharField(max_length = 200, default = '본원')
	usage = models.CharField(max_length = 200, default = '행사')
	explanation = models.TextField(blank=True, null=True)

	def explain(self):
		return self.explanation

	def id(self):
		return self.id

	def __str__(self):
		return self.name

class Reserv(models.Model):
	camp = models.CharField(max_length=200, default='')
	place = models.CharField(max_length = 200)
	booker = models.CharField(max_length = 200)
	date = models.IntegerField()
	reason = models.TextField(blank=True, null=True)