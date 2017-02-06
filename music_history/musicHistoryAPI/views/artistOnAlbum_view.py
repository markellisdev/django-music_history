from rest_framework import viewsets
from musicHistoryAPI.models import *
from musicHistoryAPI.serializers import *

class ArtistOnAlbumViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing artists on albums.
    """
    queryset = artistOnAlbum_model.ArtistOnAlbum.objects.all()
    serializer_class = artistOnAlbum_serializer.ArtistOnAlbumSerializer
