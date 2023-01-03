# this checks every other line for username
class Username:
    
        
    
    def __init__(self,UserName):
        self.userName = UserName
        
        
    file2 = open("usernamePassword.txt" , "r")
    count = 0
    for line in file2:
        count+=1
        if count %2 == 0:
            UserName=line 
        
    def __str__(self):
        # return self.id +
        return f"{self.userName}"

    
   