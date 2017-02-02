from django.db import models

class ArtistOnAlbum(models.Model):
	artistId = models.ManyToManyField(Artist)
	albumId = models.ManyToManyField(Album)