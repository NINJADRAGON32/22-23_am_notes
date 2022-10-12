#gues a number between 0-100
secret=52
ui=(input("guess a number between 0-100"))
#CHECK UI
while(not ui.isdigit()):
    ui=(input("guess a number between 0-100"))
ui=int(ui)


while (secret !=ui):
    if secret < ui:
        print("to high")
    elif secret > ui:
        print("too low")
    ui=int(input("guess a number between 0-100"))
    while(not ui.isdigit()):
        ui=(input("guess a number between 0-100"))
    ui=int(ui)

print("you got it")  