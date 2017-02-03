from rest_framework import serializers
from musicHistoryAPI.models import *

class ArtistSerializer(serializers.HyperlinkedmodelSerializer):

	class Meta:
		model = Artist
		fields = ('url', 'name', 'formed', 'influences')