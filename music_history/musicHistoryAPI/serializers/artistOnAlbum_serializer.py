from rest_framework import serializers
from musicHistoryAPI.models import *

class ArtistOnAlbumSerializer(serializers.HyperlinkedmodelSerializer):

	class Meta:
		model = ArtistOnAlbum
		fields = ('artistId', 'albumId', )