from rest_framework import serializers
from ..models import Artista, Album, Musica, Playlist, PlaylistMusica

class MusicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musica
        fields = '__all__'
        read_only_fields = ['nome', 'duracao', 'album']

class AlbumSerializer(serializers.ModelSerializer):
    artista = serializers.StringRelatedField() #Retorna o artista
    musicas = MusicaSerializer(source = 'musica_set', many=True, read_only=True)
    
    class Meta:
        model = Album
        fields = '__all__'
        read_only_fields = ['id']

class ArtistaSerializer(serializers.ModelSerializer):
    albuns = AlbumSerializer(source = 'album_set', many = True, read_only = True)
    
    class Meta:
        model = Artista
        fields = ['id', 'nome', 'pais', 'albuns']
        read_only_fields = ['id', 'pais']

class PlaylistSerializer(serializers.ModelSerializer):
    musicas = MusicaSerializer(many = True, read_only = True)
    musicas_ids = serializers.PrimaryKeyRelatedField(
        many = True,
        queryset = Musica.objects.all(), #Define de onde as musicas serao buscadas
        write_only = True
    )
    
    class Meta:
        model = Playlist
        fields = ['id', 'nome', 'musicas', 'musicas_ids']

    def create(self, validated_data):
        musicas = validated_data.pop('musicas_ids', []) #Pega as musicas que vieram no request
        playlist = Playlist.objects.create(**validated_data)
        playlist.musicas.set(musicas)
        return playlist
    
    def update(self, instance, validated_data):
        musicas = validated_data.pop('musicas_ids', []) #Pega as musicas que vieram no request
        instance.nome = validated_data.get('nome', instance.nome)
        instance.save()
        if musicas:
            instance.musicas.add(*musicas)
        return instance


class PlaylistMusicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistMusica
        fields = '__all__'