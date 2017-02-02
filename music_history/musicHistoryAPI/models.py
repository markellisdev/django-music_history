from django.db import models
from django.contrib.auth.models import User Group

# Create your models here.
class Artist(models.Model):
	name = models.CharField(max_length=55)
	formed = models.DateField()
	influences = models.CharField(max_length=240)

class Musician(models.Model):
	name = models.CharField(max_length=55)
	first_name = models.CharField(max_length=55)
	last_name = models.CharField(max_length=55)
	instrument = models.CharField(max_length=55)
	artistId = models.ForeignKey(Artist, on_delete=Models.CASCADE)

class Album(models.Model):
	title = models.CharField(max_length=240)
	release_date = models.DateField()
	duration = models.TimeField()
	artistId = models.ForeignKey(Artist, on_delete=Models.CASCADE)
	genreId = models.ForeignKey(Genre, on_delete=Models.CASCADE)

class Song(models.Model):
	title = models.CharField(max_length=140)
	duration = models.TimeField()
	artistId = ForeignKey(Artist, on_delete=Models.CASCADE)
	genreId = ForeignKey(Genre, on_delete=Models.CASCADE)

class AlbumWithSong(models.Model):

class ArtistOnAlbum(models.Model):

class Genre(models.Model):
