'''
An automated file to play random music
'''
import random
import os
MUSIC_DIR = '/Users/mac/Desktop/music'
songs = os.listdir(MUSIC_DIR)

song = random.randint(0, len(songs))

# Prints The Song Name
print(songs[song])

# For windows
# os.startfile(os.path.join(MUSIC_DIR, songs[0]))

# For mac
song_path = os.path.join(MUSIC_DIR, songs[song])
os.system('open ' + song_path)
