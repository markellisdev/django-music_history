from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from musicHistoryAPI.models import User, Artist, Album, Song, Genre, AlbumWithSong, ArtistOnAlbum, Customer
from musicHistoryAPI.serializers import UserSerializer, ArtistSerializer, AlbumSerializer, SongSerializer, GenreSerializer, AlbumWithSongSerializer, ArtistOnAlbumSerializer, CustomerSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
	"""
	A ViewSet for viewing and editing users.
	"""
	queryset = User.objects.all().order_by('-date_joined')