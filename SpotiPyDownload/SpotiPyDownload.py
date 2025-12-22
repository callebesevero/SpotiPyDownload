from spotdl import Downloader, Song, SpotifyClient
from spotdl.utils.ffmpeg import download_ffmpeg
from pathlib import Path

beforeFolders = Path(r'C:\Users\Lean\Documents\Codes\SpotiPyDownload\.venv\SpotiPyDownload\SpotiPyDownload\SpotiPyDownload.py').parent.parent
with open(rf"{beforeFolders}\.private\user.md", "r") as user:
    cont = 0
    for login in user:
        if cont == 0:
            id = login.strip()
        elif cont == 1:
            secret = login.strip()
        cont += 1
SpotifyClient.init(
    client_id=id,
    client_secret=secret
    )
musicurl = Song.search('https://open.spotify.com/intl-pt/track/3QTPW9FghnAxMRPXhzBli2?si=8c27fba64c6044b8')
music = Song.list_from_search_term(musicurl)
print(music)

saveFolder = str(input('Digite um nome para pasta na qual será(ão) salvo(s) o(s) arquivo(s) -> '))
downloader = Downloader(settings={
    'output': f'{saveFolder}'
    
})
# downloader.download_multiple_songs(music)