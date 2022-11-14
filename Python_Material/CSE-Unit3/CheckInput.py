from CheckInputClass import CheckInput


#checking to make sure the user puts in what you want
#check direct
#yes or no question
ui="Yes"
if ui=="yes" or ui=="no":
    print("checked")
else:
    print("incorrect input")

#check in a list
ui="Yes"
def checkInput(userInput,listOfAnswers):
    if ui in ["yes","Yes","no","No","NO","nah","yah"]:
        print("checked")
        return True
    else:
        print("incorrect input")
        return False

if checkInput(ui, ["yes","no","y","n"]):
    print("Keep going in program")

while(not checkInput(ui, ["yes","no","y","n"])):
    ui=input()

CheckInput.getCorrectInput(ui, ["yes","no","y","n"], "do you like cheese?")
#change input
ui = "YES"
if ui =="YES":
    print("good")
#lower and upper
print (ui.lower())
print (ui.upper())
print (ui.title()) #->first letter is capitalized in each word

#check number
if ui.isdigit(): #check to see if ui is number
    print("ui is a number")

#no special character
if (ui.isalnum()):
    print("yes")

if (ui.isalpha()):
    print("yay")