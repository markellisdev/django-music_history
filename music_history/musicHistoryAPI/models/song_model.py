from django.db import models

class Song(models.Model):
	title = models.CharField(max_length=140)
	duration = models.TimeField()
	artistId = ForeignKey(Artist, on_delete=Models.CASCADE)
	genreId = ForeignKey(Genre, on_delete=Models.CASCADE)