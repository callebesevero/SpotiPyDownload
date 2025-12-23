from spotdl import Spotdl
from pathlib import Path

with open(r'.private\auth.md') as auth:
    cont = 0
    for linha in auth:
        if cont == 0:
            id = linha
        elif cont == 1:
            secret = linha
        cont += 1

# The default spotdl auth:
spotdl = Spotdl(client_id=id, client_secret=secret)

# Catch music URL
songURL = str(input('Insira a URL da Playlist/Música -> '))
toDownload = spotdl.search([songURL])
downloaded = spotdl.download_songs(toDownload)

# Construct the path to \Downloads folder
homePath = Path().home()
downloadsPath = rf'{homePath}\Downloads'

if 'SpotiPyDownload' not in Path(downloadsPath):
    Path('SpotiPyDownload').mkdir()

# Catch the path of each downloaded song
for music in downloaded:
    print(music[-1])
print(downloaded)