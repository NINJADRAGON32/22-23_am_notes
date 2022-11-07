#declare/define this is a class
class Song:

    #what makes a song
    def __init__(self,name,artist,lyrics,albumName,genre,producer,duration,explicit):
        self.name = name 
        self.artist = artist
        self.lyrics = lyrics
        self.albumName = albumName
        self.genre = genre
        self.producer = producer
        self.duration =duration
        self.explicit = explicit
        
        
        
        
    #what does a song look like when you print it
    def __str__(self):
        out = self.name + "\n\t" + self.artist
        return out
    #getters/accesors and setter/muatators
    #techn. each variable that gets passed in needs a getter and a setter
    #get name and duration of song
    def getName(self):
        return self.name 

    def getDuration(self):
        return self.duration
    
    #set title
    def setName(self,newTitle):
        self.title=newTitle
    
    
    
    
    
    
    #other methods