from rest_framework import viewsets
from .serializers import ArtistaSerializer, AlbumSerializer, MusicaSerializer, PlaylistSerializer, PlaylistMusicaSerializer
from ..models import Artista, Album, Musica, Playlist, PlaylistMusica
from datetime import timedelta #Para trabalhar com duracao
import requests

class ArtistaViewSet(viewsets.ModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer

    def perform_create(self, serializer):
        nome_artista = serializer.validated_data['nome']
        artista_obj = serializer.save()
        
        try:
            response_artist = requests.get(f'https://musicbrainz.org/ws/2/artist/?query={nome_artista}&fmt=json')
            response_artist.raise_for_status()
            artist_data = response_artist.json()
            
            mb_artist_id = artist_data['artists'][0]['id']
            response_albums = requests.get(f'https://musicbrainz.org/ws/2/release/?artist={mb_artist_id}&fmt=json')
            response_albums.raise_for_status()
            albums_data = response_albums.json().get('releases', [])

            for album_info in albums_data:
                album_nome = album_info.get('title', '')
                data_lancamento = album_info.get('date', None)
                if data_lancamento and len(data_lancamento) == 4: #Verifica se so veio o ano
                    data_lancamento = f"{data_lancamento}-01-01"

                album_obj, created = Album.objects.get_or_create( #Cria um album ou pega o que ja existe
                    nome = album_nome,
                    artista = artista_obj,
                    defaults = {
                        'data_lancamento': data_lancamento
                    }
                )

                release_id = album_info['id']
                response_musicas = requests.get(f'https://musicbrainz.org/ws/2/recording?release={release_id}&fmt=json')
                response_musicas.raise_for_status()
                musicas_data = response_musicas.json().get('recordings', []) #Pega as musicas do album

                for musica_info in musicas_data:
                    duracao_ms = musica_info.get('length', None) #Pega a duracao em MS
                    Musica.objects.get_or_create(
                        nome = musica_info.get('title', ''),
                        duracao = timedelta(milliseconds = duracao_ms) if duracao_ms else None, #Converte os MS para timedelta, caso nao exista pega None
                        album = album_obj
                    )

        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar dados do artista {nome_artista}: {e}")

class AlbumViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class MusicaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer

class PlayListViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class PlayListMusicaViewSet(viewsets.ModelViewSet):
    queryset = PlaylistMusica.objects.all()
    serializer_class = PlaylistMusicaSerializer

    def perform_create(self, serializer):
        serializer.save()
        #O drf cria automaticamente o id