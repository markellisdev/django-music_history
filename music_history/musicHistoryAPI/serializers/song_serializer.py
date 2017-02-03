from rest_framework import serializers
from musicHistoryAPI.models import *

class SongSerializer(serializers.HyperlinkedmodelSerializer):

	class Meta:
		model = Song
		fields = ('title', 'duration', 'artistId', 'genreId')