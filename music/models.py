from django.db import models

# Create your models here.


class Playlist(models.Model):
    playlist_title = models.CharField(max_length=250, default="")
    playlist_logo = models.CharField(max_length=250, default="")
    playlist_subtitle = models.CharField(max_length=250, default="")

    def __str__(self):
        return self.playlist_title


class Song(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250, default="")
    album_title = models.CharField(max_length=250, default="")
    added_data = models.CharField(max_length=250, default="")
    duration = models.CharField(max_length=250, default="")
    artist = models.CharField(max_length=250, default="")
    song_logo = models.CharField(max_length=250, default="")
    song_mp3 = models.FileField(upload_to="mp3/", default="")

    def __str__(self):
        return self.song_title


class WelcomePlaylist(models.Model):
    playlist_title = models.CharField(max_length=250, default="")
    playlist_logo = models.CharField(max_length=250, default="")

    def __str__(self):
        return self.playlist_title


class MadeforyouPlaylist(models.Model):
    playlist_title = models.CharField(max_length=250, default="")
    playlist_logo = models.CharField(max_length=250, default="")
    playlist_subtitle = models.CharField(max_length=250, default="")

    def __str__(self):
        return self.playlist_title


class RecentPlaylist(models.Model):
    playlist_title = models.CharField(max_length=250, default="")
    playlist_logo = models.CharField(max_length=250, default="")
    playlist_subtitle = models.CharField(max_length=250, default="")

    def __str__(self):
        return self.playlist_title
