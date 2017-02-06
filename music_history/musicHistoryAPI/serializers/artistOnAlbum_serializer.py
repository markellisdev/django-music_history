from rest_framework import serializers
from musicHistoryAPI.models import *

class ArtistOnAlbumSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = artistOnAlbum_model.ArtistOnAlbum
        fields = ('artistId', 'albumId', )
