from rest_framework import viewsets, generics
from musicHistoryAPI.models import *
from musicHistoryAPI.serializers import *

class MusicianViewSet(viewsets.ModelViewSet):
	"""
	A ViewSet for viewing and editing musicians.
	"""
	queryset = Musician.objects.all()
	serializer_class = musician_serializer.MusicianSerializer