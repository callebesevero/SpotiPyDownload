from spotdl import Downloader, Song, SpotifyClient
from spotdl.utils.ffmpeg import download_ffmpeg
import os

with open(".private\\user.md", "r") as user:
    cont = 0
    for login in user:
        if cont == 0:
            id = login
        elif cont == 1:
            secret = login
        cont += 1
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