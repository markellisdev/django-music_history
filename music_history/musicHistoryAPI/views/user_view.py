from django.contrib.auth.models import User
from rest_framework import viewsets, serializers, generics
from musicHistoryAPI.serializers import *

class UserViewSet(viewsets.ModelViewSet):
	"""
	A ViewSet for viewing and editing users.
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = user_serializer.UserSerializer