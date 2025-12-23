from spotdl import Spotdl
from pathlib import Path
from shutil import move
from texto import formatar

# The default spotdl auth:
Spotdl.__init__
id = 'f8a606e5583643beaa27ce62c48e3fc1'
secret = 'f6f4c8f73f0649939286cf417c811607'
spotdl = Spotdl(client_id=id, client_secret=secret)

# Construct the path to \Downloads folder
homePath = Path().home()
downloadsPath = rf'{homePath}\Downloads'

# Verify if 'SpotiPyDownloader' folder exists
if not Path(rf'{downloadsPath}\SpotiPyDownload').exists():
    Path(rf'{downloadsPath}\SpotiPyDownload').mkdir()

while True:
    # Get music URL
    songURL = str(input('Insira a URL da Playlist/Música [SAIR/S/ENTER para fechar] -> ').strip())
    if songURL.upper() in 'SAIR':
        break

    toDownload = spotdl.search([songURL])
    downloaded = spotdl.download_songs(toDownload)

    # Get the path of each downloaded song
    for music in downloaded:
        move(music[-1], rf'{downloadsPath}\SpotiPyDownload')