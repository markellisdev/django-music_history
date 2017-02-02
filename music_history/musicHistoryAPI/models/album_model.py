from django.db import models

class Album(models.Model):
	title = models.CharField(max_length=240)
	release_date = models.DateField()
	duration = models.TimeField()
	artistId = models.ForeignKey(Artist, on_delete=Models.CASCADE)
	genreId = models.ForeignKey(Genre, on_delete=Models.CASCADE)