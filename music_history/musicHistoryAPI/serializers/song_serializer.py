from rest_framework import serializers
from musicHistoryAPI.models import *

class SongSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = song_model.Song
        fields = ('title', 'duration', 'artistId', 'genreId')
