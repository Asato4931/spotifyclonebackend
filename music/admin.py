from django.contrib import admin

from .models import Playlist, Song, WelcomePlaylist, MadeforyouPlaylist, RecentPlaylist

admin.site.register(Playlist)
admin.site.register(Song)

admin.site.register(WelcomePlaylist)
admin.site.register(MadeforyouPlaylist)
admin.site.register(RecentPlaylist)
