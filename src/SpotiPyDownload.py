from spotdl.search import SpotifyClient
from spotdl import search
from spotdl.download.downloader import DownloadManager
from pathlib import Path
from shutil import move
from dotenv import load_dotenv
from os import getenv

print('Espere... Carregando ferramentas!')

# Auth:
load_dotenv()
client_id=getenv("SPOTIPY_CLIENT_ID")
client_secret=getenv('SPOTIPY_CLIENT_SECRET')

spotdl = SpotifyClient.init(
    client_id=client_id, 
    client_secret=client_secret,
    user_auth=False
    )

downloadsPath = Path.home() / "Downloads"
targetDir = downloadsPath / "SpotiPyDownload"
targetDir.mkdir(parents=True, exist_ok=True)

while True:
    # Get music URL
    songURL = str(input('Insira a URL da Playlist/Música [SAIR/S/ENTER para fechar] -> ').strip())
    if songURL.upper() in 'SAIR':
        break

    toDownload = search([songURL])
    downloaded = DownloadManager.download_song(toDownload)

    # Get the path of each downloaded song
    for music in downloaded:
        move(music[-1], targetDir)