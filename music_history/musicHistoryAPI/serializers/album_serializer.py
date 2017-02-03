from rest_framework import serializers
from musicHistoryAPI.models import *
from musicHistoryAPI.serializers import *

class AlbumSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Album
		fields = ('url', 'title', 'release_date', 'duration', 'artistId', 'genreId')