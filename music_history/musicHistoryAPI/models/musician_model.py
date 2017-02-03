from django.db import models
from . import *

class Musician(models.Model):
	name = models.CharField(max_length=55)
	first_name = models.CharField(max_length=55)
	last_name = models.CharField(max_length=55)
	instrument = models.CharField(max_length=55)
	artistId = models.ForeignKey(artist_model.Artist, on_delete=models.CASCADE)