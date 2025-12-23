from spotdl import Spotdl
from pathlib import Path
from shutil import move
from os.path import dirname, abspath, join

print('Espere... Carregando ferramentas!')

# Auth:
dirScript = dirname(abspath(__file__))
archive = join(dirScript, "user.txt")
with open(archive, "r") as user:
    cont = 0
    for login in user:
        if cont == 0:
            id = login.strip()
        elif cont == 1:
            secret = login.strip()
        cont += 1
spotdl = Spotdl(
    client_id=id, 
    client_secret=secret,
    user_auth=False
    )

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