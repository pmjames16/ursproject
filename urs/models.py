from django.db import models
#from django.utils import timezone


class Place(models.Model):
	name = models.CharField(max_length = 200)
	camp = models.CharField(max_length = 200, default = 'bonwon')
	reserved = {}

	def available(self, time):
		if (time in self.reserved):
			return False
		return True

	def reservate(self, times):
		for time in times:
			self.reserved[time] = 'r'

	def __str__(self):
		return self.name

