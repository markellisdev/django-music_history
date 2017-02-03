from django.db import models
from .artist_model import Artist
from .genre_model import Genre

class Album(models.Model):
	title = models.CharField(max_length=240)
	release_date = models.DateField()
	duration = models.TimeField()
	artistId = models.ForeignKey(Artist, on_delete=models.CASCADE)
	genreId = models.ForeignKey(Genre, on_delete=models.CASCADE)