from django.db import models

class AlbumWithSong(models.Model):
	albumId = models.ManyToManyField(Album)
	songId = models.ManyToManyField(Song)