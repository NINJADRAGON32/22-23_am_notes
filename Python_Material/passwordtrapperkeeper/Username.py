# this checks every other line for username
file2 = open("usernamePassword.txt" , "r")
count = 0
for line in file2:
    count+=1
    if count %2 == 0:
        userName=line


class Username:
    def __init__(self,userName):
        self.userName = userName
        
    def __str__(self):
        # return self.id +
        return f"{self.userName}"
    
   