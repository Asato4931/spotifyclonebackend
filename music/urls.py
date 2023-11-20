from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "music"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:playlist_id>/", views.detail, name="detail"),
    path("playlists/", views.get_playlists, name="get_playlists"),
    path(
        "madeforyouplaylists/",
        views.get_madeforyouplaylists,
        name="get_madeforyouplaylists",
    ),
    path(
        "welcomeplaylists/",
        views.get_welcomeplaylists,
        name="get_welcomeplaylists",
    ),
    path(
        "recentplaylists/",
        views.get_recentplaylists,
        name="get_recentplaylists",
    ),
    path(
        "お気に入りの曲/songs/",
        views.get_songs,
        name="get_songs",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
