from django.db import models
from . import artist_model, genre_model

class Song(models.Model):
    title = models.CharField(max_length=140)
    duration = models.TimeField()
    artistId = models.ForeignKey(artist_model.Artist, on_delete=models.CASCADE)
    genreId = models.ForeignKey(genre_model.Genre, on_delete=models.CASCADE)
