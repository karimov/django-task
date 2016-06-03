from __future__ import unicode_literals

from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
    	return self.name

class Classroom(models.Model):
	school = models.ForeignKey('School')
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Student(models.Model):
	classroot = models.ForeignKey('Classroom')
	first_name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128)

	def __str__(self):
		return self.first_name+", "+self.last_name