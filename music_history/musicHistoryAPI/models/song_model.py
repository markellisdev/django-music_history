from django.db import models
from . import *

class Song(models.Model):
	title = models.CharField(max_length=140)
	duration = models.TimeField()
	artistId = ForeignKey(artist_model.Artist, on_delete=models.CASCADE)
	genreId = ForeignKey(genre_model.Genre, on_delete=models.CASCADE)