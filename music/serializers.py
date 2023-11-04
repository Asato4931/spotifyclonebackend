from rest_framework import serializers
from django.conf import settings
from .models import Playlist, Song


class PlaylistSerializer(serializers.ModelSerializer):
    playlist_logo = serializers.SerializerMethodField()

    class Meta:
        model = Playlist
        fields = ["playlist_title", "playlist_logo", "playlist_subtitle"]

    def get_playlist_logo(self, playlist):
        if playlist.playlist_logo:
            return f"{settings.STATIC_URL}{playlist.playlist_logo}"
        return None


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = [
            "song_title",
            "album_title",
            "added_data",
            "duration",
            "artist",
            "song_logo",
            "song_mp3",
        ]
