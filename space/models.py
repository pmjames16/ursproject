from django.db import models
from django.utils import timezone

class Place(models.Model):
	name = models.CharField(max_length = 200)
	reserved = {}

	def reservate(self, date, start_time, end_time):
		for i in range(int(start_time), int(end_time)+1):
			time = date + str(int(start_time)+i)
			if (time in self.reserved):
				return false
		for i in range(int(start_time), int(end_time)+1):
			time = date + str(int(start_time)+i)
			self.reserved[date] = 'r'

	def __str__(self):
		return self.name
