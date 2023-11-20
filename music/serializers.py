from rest_framework import serializers
from django.conf import settings
from .models import Playlist, Song, MadeforyouPlaylist, RecentPlaylist, WelcomePlaylist


class PlaylistSerializer(serializers.ModelSerializer):
    playlist_logo = serializers.SerializerMethodField()

    class Meta:
        model = Playlist
        fields = ["playlist_title", "playlist_logo", "playlist_subtitle"]

    def get_playlist_logo(self, playlist):
        if playlist.playlist_logo:
            return f"{settings.STATIC_URL}{playlist.playlist_logo}"
        return None


class MadeforyouPlaylistSerializer(serializers.ModelSerializer):
    playlist_logo = serializers.SerializerMethodField()

    class Meta:
        model = MadeforyouPlaylist
        fields = ["playlist_title", "playlist_logo", "playlist_subtitle"]

    def get_playlist_logo(self, madeforyouplaylist):
        if madeforyouplaylist.playlist_logo:
            return f"{settings.STATIC_URL}{madeforyouplaylist.playlist_logo}"
        return None


class WelcomePlaylistSerializer(serializers.ModelSerializer):
    playlist_logo = serializers.SerializerMethodField()

    class Meta:
        model = WelcomePlaylist
        fields = ["playlist_title", "playlist_logo"]

    def get_playlist_logo(self, welcomeplaylist):
        if welcomeplaylist.playlist_logo:
            return f"{settings.STATIC_URL}{welcomeplaylist.playlist_logo}"
        return None


class SongSerializer(serializers.ModelSerializer):
    song_logo = serializers.SerializerMethodField()

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

    def get_song_logo(self, song):
        if song.song_logo:
            return f"{settings.STATIC_URL}{song.song_logo}"
        return None

    def get_song_mp3(self, song):
        if song.song_mp3:
            request = self.context.get("request")
            return request.build_absolute_uri(song.song_mp3.url)
        return None


class RecentPlaylistSerializer(serializers.ModelSerializer):
    playlist_logo = serializers.SerializerMethodField()

    class Meta:
        model = RecentPlaylist
        fields = ["playlist_title", "playlist_logo", "playlist_subtitle"]

    def get_playlist_logo(self, recentplaylist):
        if recentplaylist.playlist_logo:
            return f"{settings.STATIC_URL}{recentplaylist.playlist_logo}"
        return None
