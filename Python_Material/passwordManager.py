

#signing up
username = input("username: ")
password = input("password: ")
UI = (username , password)
fileToWriteTo = open("usernamePassword.txt","w")
fileToWriteTo.write(str(UI))
fileToWriteTo.close()


#signing in 
user = input("Username: ")
pas = input("Password: ")
ui = (user , pas)
file2 = open("usernamePassword.txt" , "r")
login = file2.readlines()
for line in login:
    login=(line.rstrip())
print(login)
if ui == login:
    print("u did it!!")
else: 
    print("it no work ")

