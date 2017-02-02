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

class Song(models.Model):

class AlbumWithSong(models.Model):

class ArtistOnAlbum(models.Model):

class Genre(models.Model):
