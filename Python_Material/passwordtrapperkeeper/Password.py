# this checks every other line for username
file2 = open("usernamePassword.txt" , "r")
count = 1
for line in file2:
    count+=1
    if count %2 == 0:
        passWord=line


class Password:
    def __init__(self,passWord):
        self.passWord = passWord
        
    def __str__(self):
        # return self.id +
        return f"{self.passWord}"