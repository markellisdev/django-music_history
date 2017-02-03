from rest_framework import serializers
from musicHistoryAPI.models import *

class GenreSerializer(serializers.HyperlinkedmodelSerializer):

	class Meta:
		model = Artist
		fields = ('title', )