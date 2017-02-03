from rest_framework import viewsets, generics
from musicHistoryAPI.models import *
from musicHistoryAPI.serializers import *

class AlbumViewSet(viewsets.ModelViewSet):
	"""
	A ViewSet for viewing and editing Albums.
	"""
	queryset = Album.objects.all()
	serializer_class = album_serializer.AlbumSerializer