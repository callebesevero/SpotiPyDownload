from spotdl import Downloader, Song, SpotifyClient
from spotdl.utils.ffmpeg import download_ffmpeg
import os

id = str(input('Qual o client do Spotify? -> ').strip())
secret = str(input('Qual a senha do Spotify? -> ').strip())
SpotifyClient.init(
    client_id=id,
    client_secret=secret
    )
músicas = Song.list_from_search_term('https://open.spotify.com/intl-pt/track/1Z6Ex3aZdoom5j6LHfHIB5')
downloader = Downloader(settings={
    "fetch_albums": True, # Ou False, dependendo do seu uso
    # outras configurações aqui...
})
Downloader.download_multiple_songs(download_ffmpeg, songs=músicas)