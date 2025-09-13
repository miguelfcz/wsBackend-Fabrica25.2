from django.db import models

class Artista(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return f"Artista: {self.nome}, id: {self.id}, país: {self.pais}"

class Album(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    data_lancamento = models.DateField()
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)

    def __str__ (self):
        return f"Album: {self.nome}, id: {self.id}, data de lançamento: {self.data_lancamento}, artista: {self.artista}"
    
class Musica(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    duracao = models.DurationField(null = True, blank = True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f"Musica: {self.nome}, id: {self.id}, duração: {self.duracao}, album: {self.album}"
    
class Playlist(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    musicas = models.ManyToManyField(Musica, related_name='playlists') #Varias músicas

    def __str__(self):
        return f"Playlist: {self.nome}, id: {self.id}, múscas: {self.musicas}"
    
class PlaylistMusica(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    musica = models.ForeignKey(Musica, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Playlist.nome}, {self.Playlist.musica}"