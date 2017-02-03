from django.db import models
from . import *

class AlbumWithSong(models.Model):
	albumId = models.ManyToManyField(album_model.Album)
	songId = models.ManyToManyField(song_model.Song)