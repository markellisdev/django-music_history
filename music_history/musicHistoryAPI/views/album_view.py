from rest_framework import viewsets, generics
from musicHistoryAPI.models import *
from musicHistoryAPI.serializers import *

class AlbumViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Albums.
    """
    queryset = album_model.Album.objects.all()
    serializer_class = album_serializer.AlbumSerializer
