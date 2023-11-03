from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "music"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:playlist_id>/", views.detail, name="detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
