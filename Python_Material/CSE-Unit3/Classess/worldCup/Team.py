class Team:
    #constructor
    def ___init___(self,name,wins,points,injuries):
        self.name=name
        self.wins=wins
        self.points=points
        self.injuries=injuries

    #to string function
    def __str__(self):
        return self.name
    
    #getters and setters
    def addPoints(self,newPoints):
        self.points+=newPoints
    
    def addwins(self):
        self.wins+=1
        
    def overALLStats(self):
        out = f'''
        {self.name}:
            wins:{self.wins}
            points:{self.points}
            booboos: {self.injuries}
        '''
        return out
    
        #record: (W,D,L)
        def record(self):
            out= f'({self.wins},d,l)'
            return out