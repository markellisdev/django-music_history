from rest_framework import viewsets, generics
from musicHistoryAPI.models import *
from musicHistoryAPI.serializers import *

class ArtistViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing artists.
    """
    queryset = artist_model.Artist.objects.all()
    serializer_class = artist_serializer.ArtistSerializer