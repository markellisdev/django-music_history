from rest_framework import serializers
from musicHistoryAPI.models import *

class AlbumWithSongSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = albumWithSong_model.AlbumWithSong
        fields = ('albumId', 'songId')
