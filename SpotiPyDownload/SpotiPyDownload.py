from spotdl import Spotdl

spotdl = Spotdl(client_id="f8a606e5583643beaa27ce62c48e3fc1", client_secret="f6f4c8f73f0649939286cf417c811607")
songURL = str(input('Insira a URL da Playlist/Música -> '))
toDownload = spotdl.search([songURL])
spotdl.download_songs(toDownload)