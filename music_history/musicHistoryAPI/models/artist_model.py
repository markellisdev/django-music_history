from django.db import models

class Artist(models.Model):
	name = models.CharField(max_length=55)
	formed = models.DateField()
	influences = models.CharField(max_length=240)