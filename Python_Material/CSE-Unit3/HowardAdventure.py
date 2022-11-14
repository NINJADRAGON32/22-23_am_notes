# cd .\Documents\22-23_am_notes\Python_Material\CSE-Unit3\ 
#this is my little adventure 
#I will have the user search through the forrest in search of a buried time capsule that has millions of dollars worth in bitcoin on a usb drive 
#this takes inspiration from the terminus game
timeCapsule="timeCapsule"
inventory=[]
shovel="shovel"
beans="beans"
#clue("often times one must return from whence they came to find their success")
#procedures
def deathByLandmine():
    print("\033[1;31;40m you hit a landmine. congrats you are know more than two places at once \n")







print("NEED TO KNOW: all inputs will be highlighted in White /n")

greetings=input("Hello adventurer:  \n")
if greetings not in ["hello","Hello","hewo","Hewo","hi","Hi","hey","Hey","Whats Up","whats up", "Whats up"]:
    print("wow, not very friendly are we. Anyways...")
print ("Here's your mission: deep in the woods their lays buried a treasure, your mission is to find the treasure and avoid digging up land mines.")
readyOrNot=input("Are you ready?(y/n):  \n")
if readyOrNot=="n":
    print(" WELL TOO BAD!!")

while timeCapsule not in inventory:
    print("you are currently at your RV")
    whereToGo=input("before you, you see \n(1): A wooden path with an image of a swamp next to it \n(2): a deer path that could lead anywhere \n(3): A firetower atop a hill \n(4): a trail map \n(5): A gravel trail leading off to the right with a marker with an apple symbol next to it \n(6): A gravel trail in the middle with a marker with what looks to be a potato symbol next to it \n(7): behind you which lies a big redwood tree  \n where do you wish to go(enter the number in front of each path) \n")
    if whereToGo=="2":
        print("you chose the deer path")
        print("the path leads you to the entrance of a cave where some deer graze.")
        print("one of the deer hears you, the deer starts to run as it exits the clearing you hear a boom... The deer hit a landmine. You must be carefull moving forward")
        whatToDo=input("would you like to (1) check out the dead dear (2) enter the cave (3) run around in circles (4) turn around and go home \n")
        if whatToDo=="1":
            deathByLandmine()
        elif whatToDo=="3":
            deathByLandmine()
        elif whatToDo=="2":
            while shovel not in inventory:
                print("you are now in the cave. theres not much in there except for some bat poo, what looks to be the ruins of a camp, and a shovel ")
                pickup=input("What would you like to do: \n(1) exit the cave and go home \n(2) pickup the shovel \n(3) search through the camp for resources \n(4) explore the cave further \n")
                if pickup == ("1"):
                    print("why are you leaving the cave don't you think you need the shovel?\n")
                elif pickup == ("2"):
                    print("yay, your one step closer to finding the timecapsule\n")
                    inventory.append(shovel)
                elif pickup ==("3"):
                    print("you found a can of beans\n") 
                    inventory.append(beans)
                elif pickup ==("4"):
                    print("its a cave, it's dark, you're scared of the dark, you return to the entrance of the cave out of fear, screaming like a girl on your way there\n ")
    elif whereToGo == ("1"):
        print("you follow the path and sure enough it leads to a swamp.\n \n You explore further. \n You find in the swamp a hut made out of what looks to be a tree stump a massive mud pool and an outhouse ")
        whereToGo=input("you can \n(1) knock on the door \n(2)get outta there \n(3) put your finger and your thumb in the shape of an L on your forehead \n(4) go to the outhouse")
    
    
    
    
    
    
    
    
    
    
    
    
    
    #temperary iterator
    else: 
        inventory.append(timeCapsule)
                    


