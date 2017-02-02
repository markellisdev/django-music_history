from django.db import models

class Musician(models.Model):
	name = models.CharField(max_length=55)
	first_name = models.CharField(max_length=55)
	last_name = models.CharField(max_length=55)
	instrument = models.CharField(max_length=55)
	artistId = models.ForeignKey(Artist, on_delete=Models.CASCADE)