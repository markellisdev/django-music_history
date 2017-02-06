from rest_framework import serializers
from musicHistoryAPI.models import *

class AlbumSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = album_model.Album
        fields = ('url', 'title', 'release_date', 'duration', 'artistId', 'genreId')
