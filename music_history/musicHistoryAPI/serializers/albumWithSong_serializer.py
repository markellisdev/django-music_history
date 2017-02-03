from rest_framework import serializers
from musicHistoryAPI.models import *

class AlbumWithSongSerializer(serializers.HyperlinkedmodelSerializer):

	class Meta:
		model = AlbumWithSong
		fields = ('albumId', 'songId')