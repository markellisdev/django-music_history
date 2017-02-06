from django.db import models
from .album_model import Album
from .artist_model import Artist

class ArtistOnAlbum(models.Model):
	artistId = models.ManyToManyField(Artist)
	albumId = models.ManyToManyField(Album)