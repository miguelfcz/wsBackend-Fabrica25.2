from django.urls import path, include
from rest_framework import routers

from .api.viewsets import ArtistaViewSet, AlbumViewSet, MusicaViewSet, PlayListViewSet, PlayListMusicaViewSet

from .views import (
    ArtistaListView, ArtistaDetailView,
    AlbumListView, AlbumDetailView,
    MusicaListView, MusicaDetailView,
    PlaylistListView, PlaylistDetailView,
)

router = routers.DefaultRouter()
router.register('artista', ArtistaViewSet, basename='artista')
router.register('album', AlbumViewSet, basename='album')
router.register('musica', MusicaViewSet, basename='musica')
router.register('playlist', PlayListViewSet, basename='playlist')
router.register('playlistmusica', PlayListMusicaViewSet, basename='playlistmusica')

urlpatterns = router.urls + [
    path('artistas/', ArtistaListView.as_view(), name='artistas'),
    path('artistas/<int:pk>/', ArtistaDetailView.as_view(), name='artista-detail'),
    path('albuns/', AlbumListView.as_view(), name='albuns'),
    path('albuns/<int:pk>/', AlbumDetailView.as_view(), name='album-detail'),
    path('musicas/', MusicaListView.as_view(), name='musicas'),
    path('musicas/<int:pk>/', MusicaDetailView.as_view(), name='musica-detail'),
    path('playlists/', PlaylistListView.as_view(), name='playlists'),
    path('playlists/<int:pk>/', PlaylistDetailView.as_view(), name='playlist-detail'),

    path('', ArtistaListView.as_view(), name='home'),
]