from django.shortcuts import render, get_object_or_404

from .models import Playlist, MadeforyouPlaylist, WelcomePlaylist, RecentPlaylist, Song

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Playlist
from .serializers import (
    PlaylistSerializer,
    MadeforyouPlaylistSerializer,
    WelcomePlaylistSerializer,
    RecentPlaylistSerializer,
    SongSerializer,
)


def index(request):
    all_playlists = Playlist.objects.all()

    return render(request, "music/index.html", {"all_playlists": all_playlists})


def detail(request, playlist_id):
    playlist = get_object_or_404(Playlist, pk=playlist_id)

    return render(request, "music/detail.html", {"playlist": playlist})


@api_view(["GET"])
def get_playlists(request):
    playlists = Playlist.objects.all()
    serializer = PlaylistSerializer(playlists, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_madeforyouplaylists(request):
    madeforyouplaylists = MadeforyouPlaylist.objects.all()
    serializer = MadeforyouPlaylistSerializer(madeforyouplaylists, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_welcomeplaylists(request):
    welcomeplaylists = WelcomePlaylist.objects.all()
    serializer = WelcomePlaylistSerializer(welcomeplaylists, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_recentplaylists(request):
    recentplaylists = RecentPlaylist.objects.all()
    serializer = RecentPlaylistSerializer(recentplaylists, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_songs(request):
    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True, context={"request": request})
    return Response(serializer.data)
