class Ui:
    def __init__(self,user,pas):
        self.user = user
        self.pas = pas
        
    def __str__(self):
        # return self.id +
        return f"{self.user} {self.pas}"