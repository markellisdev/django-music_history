from rest_framework import viewsets
from musicHistoryAPI.models import *
from musicHistoryAPI.serializers import *

class ArtistOnAlbumViewSet(viewsets.ModelViewSet):
	"""
	A ViewSet for viewing artists on albums.
	"""
	queryset = ArtistOnAlbum.objects.all()
	serializer_class = ArtistOnAlbumSerializer