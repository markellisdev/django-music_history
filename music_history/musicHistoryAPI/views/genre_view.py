from rest_framework import viewsets
from musicHistoryAPI.models import *
from musicHistoryAPI.serializers import *

class GenreViewSet(viewsets.ModelViewSet):
	"""
	A ViewSet for viewing and editing genres.
	"""
	queryset = Genre.objects.all()
	serializer_class = genre_serializer.GenreSerializer