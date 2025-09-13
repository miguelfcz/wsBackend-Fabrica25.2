from django.views.generic import ListView, DetailView
from .models import Artista, Album, Musica, Playlist

class ArtistaListView(ListView):
    model = Artista
    template_name = 'artista_list.html'
    context_object_name = 'artistas'

    def get_queryset(self):
        return Artista.objects.prefetch_related('album_set')

class ArtistaDetailView(DetailView):
    model = Artista
    template_name = 'artista_detail.html'
    context_object_name = 'artista'

class AlbumListView(ListView):
    model = Album
    template_name = 'album_list.html'
    context_object_name = 'albuns'

    def get_queryset(self):
        return Album.objects.select_related('artista').prefetch_related('musica_set')

class AlbumDetailView(DetailView):
    model = Album
    template_name = 'album_detail.html'
    context_object_name = 'album'

class MusicaListView(ListView):
    model = Musica
    template_name = 'musica_list.html'
    context_object_name = 'musicas'

class MusicaDetailView(DetailView):
    model = Musica
    template_name = 'musica_detail.html'
    context_object_name = 'musica'

class PlaylistListView(ListView):
    model = Playlist
    template_name = 'playlist_list.html'
    context_object_name = 'playlists'

class PlaylistDetailView(DetailView):
    model = Playlist
    template_name = 'playlist_detail.html'
    context_object_name = 'playlist'