from rest_framework import serializers
from musicHistoryAPI.models import *

class MusicianSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = musician_model.Musician
        fields = ('name', 'first_name', 'last_name', 'instrument', 'artistId')
