from django.db import models
from .album_model import Album
from .song_model import Song

class AlbumWithSong(models.Model):
	albumId = models.ManyToManyField(Album)
	songId = models.ManyToManyField(Song)