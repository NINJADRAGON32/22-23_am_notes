from Ui import Ui
from Username import Username
from Password import Password
import Password
import Username

userName = Username.Username
passWord = Password.passWord
account = input ("do you already have an account(y/n): ")
if account == 'n':
    #######signing up#######
    username = input("username: ")
    password = input("password: ")
    fileToWriteTo = open("usernamePassword.txt","a")
    fileToWriteTo.write(str(username) + "\n" + str(password) + "\n" )
    fileToWriteTo.close()
    ####signing up#######
     
print("please sign in: ")
#######signing in########
user = input("Username: ")
pas = input("Password: ")
########signing in#######

#temporary###################
ui = Ui(user, pas)
accountUsername = Username(Username)
accountPassword = Password(passWord)
print(ui.pas)
print(accountPassword.passWord)
#temporary###################

print(type(ui.user),type(accountUsername.userName))
print(type(ui.pas),type(accountPassword.passWord))
if ui.user == accountUsername.userName and ui.pas == accountPassword.passWord:
    print("u did it!!")
else: 
    print("it no work ")



