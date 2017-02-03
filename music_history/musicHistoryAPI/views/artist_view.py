from rest_framework import viewsets, generics
from musicHistoryAPI.serializers import *
from musicHistoryAPI.models import *

class ArtistViewSet(viewsets.ModelViewSet):
	"""
	A ViewSet for viewing and editing artists.
	"""
	queryset = Artist.objects.all()
	serializer_class = artist_serializer.ArtistSerializer