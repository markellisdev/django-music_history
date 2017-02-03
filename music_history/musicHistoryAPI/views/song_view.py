from rest_framework import viewsets
from musicHistoryAPI.models import *
from musicHistoryAPI.serializers import *

class SongViewSet(viewsets.ModelViewSet):
	"""
	A ViewSet for viewing and editing songs.
	"""
	queryset = Song.objects.all()
	serializer_class = SongSerializer