from django.config.auth.models import User
from rest_framework import serializers
from musicHistoryAPI.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class defines the fields that get serialized/deserialized, related
    to :model:`auth.User`
    author: Ali Kimbrell
    """
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'groups', )