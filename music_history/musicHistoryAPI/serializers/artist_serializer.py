from rest_framework import serializers
from musicHistoryAPI.models import *

class ArtistSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = artist_model.Artist
        fields = ('url', 'name', 'formed', 'influences')
