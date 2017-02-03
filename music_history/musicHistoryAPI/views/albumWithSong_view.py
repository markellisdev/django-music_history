from rest_framework import viewsets
from musicHistoryAPI.models import *
from musicHistoryAPI.serializers import *

class AlbumWithSongViewSet(viewsets.ModelViewSet):
	"""
	A ViewSet for viewing and editing genres.
	"""
	queryset = AlbumWithSong.objects.all()
	serializer_class = AlbumWithSongSerializer