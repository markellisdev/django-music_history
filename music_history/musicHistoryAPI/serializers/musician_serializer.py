from rest_framework import serializers
from musicHistoryAPI.models import *

class MusicianSerializer(serializers.HyperlinkedmodelSerializer):

	class Meta:
		model = Musician
		fields = ('name', 'first_name', 'last_name', 'instrument', 'artistId')