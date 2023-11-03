from django.shortcuts import render, get_object_or_404

from .models import Playlist

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Playlist


def index(request):
    all_playlists = Playlist.objects.all()

    return render(request, "music/index.html", {"all_playlists": all_playlists})


def detail(request, playlist_id):
    playlist = get_object_or_404(Playlist, pk=playlist_id)

    return render(request, "music/detail.html", {"playlist": playlist})


@api_view(["GET"])
def get_playlists(request):
    playlists = Playlist.objects.all().values(
        "playlist_title", "playlist_logo", "playlist_subtitle"
    )
    return Response(list(playlists))
