import os
import eyed3
from shutil import copy

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
os.chdir(desktop)

src = os.path.join(os.getcwd(), 'Music')
dst = os.path.join(os.getcwd(), 'NewMusic')

count = 0

for subdir, dirs, files in os.walk(src):
    for file in files:
        songPath = os.path.join(subdir, file)
        print(songPath)
        song = eyed3.load(songPath)
        artist = song.tag.album_artist
        album = song.tag.album
        artistFolder = os.path.join(dst, artist)
        albumFolder = os.path.join(artistFolder, album)
        if not (os.path.exists(artistFolder)): #if the artist folder does not exist, create
            os.makedirs(artistFolder)
        if not (os.path.exists(albumFolder)): #if the album folder does not exist, create
            os.makedirs(albumFolder)

        newSongPath = os.path.join(albumFolder,file)

        if not (os.path.exists(newSongPath)): #if the song does not exist, copy
            count += 1
            copy(songPath, albumFolder)
            print("Copied", file)
        else:
            print("Song already exists")


print(count, "songs were added")


