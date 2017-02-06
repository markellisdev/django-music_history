from rest_framework import serializers
from musicHistoryAPI.models import *

class GenreSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = artist_model.Artist
        fields = ('title', )
