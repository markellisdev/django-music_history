from django.contrib.auth.models import User
from rest_framework import serializers
from musicHistoryAPI.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class defines the fields that get serialized/deserialized, related
    to :model:`auth.User`
    author: Mark Ellis
    """
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'groups', )
