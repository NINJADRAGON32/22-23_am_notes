#name, artist, duration, lyrics, albumName, explicit, genre, producer
#string, string, int, string, string, boolean, string, string

#4:38 -> 4*60+38   int - 8 bits or 1 byte
#4:38 -> 4+38/60   float- 32 bits
# "4:38" -> "4:38" string - each character takes up a byte

from song import Song


name, artist, lyrics, albumName, genre, producer= "","","","","",""
duration=0
explicit = False


library=[]
ui=""
while ui!= ("stop"):
    #construct a song
    newSong = Song(input("name: "),
         input("artist: "),
         input("lyrics: "),
         input("albumName: "),
         input("genre: "),
         input("producer: "),
         int(input("duration: ")),
         bool(input("explicit: ")),
    )
    library.append(newSong)
    ui=input("would you like to continue or stop?")

for song in library:
    print(song)

#How long is Sweet Child O Mine

songToFind=input("which song?")
for song in library:
    if song.getName()==songToFind:
        print(song.getDuration())
    
    
    
    
    
    
    
    
'''while song!= ("stop"):
    song=[]
    song.append(input("name: "))
    song.append(input("artist: "))
    song.append(input("lyrics: "))
    song.append(input("albumName: "))
    song.append(input("genre: "))
    song.append(input("producer: "))
    song.append(int(input("duration: ")))
    song.append(bool(input("name: ")))
    library.append(song)
    song=input("would you like to continue or stop?")
'''    