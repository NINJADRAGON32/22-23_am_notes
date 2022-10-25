#this is my little adventure 
#I will have the user search through the forrest in search of a buried time capsule that has millions of dollars worth in bitcoin on a usb drive 
#this takes inspiration from the terminus game

greetings=input("Hello adventurer: ")
if greetings not in ["hello","Hello","hewo","Hewo","hi","Hi","hey","Hey","Whats Up","whats up", "Whats up"]:
    print("wow, not very friendly are we. Anyways...")
print ("Here's your mission: deep in the woods their lays buried a treasure, your mission is to find the treasure and avoid digging up land mines.")
readyOrNot=input("Are you ready?(y/n): ")
if readyOrNot=="n":
    print("WELL TOO BAD!!")

print("you are currently at your RV")
whereToGo=input("before you, you see (1): smoke in the distance (2): a deer path that could lead anywhere (3): A firetower atop a hill (4): a trail map (5): A gravel trail leading off to the right with a marker with an apple symbol next to it (6): A gravel trail in the middle with a marker with what looks to be a potato symbol next to it (7): behind you which lies a big redwood tree (8): A wooden floored path with a marker with an image of a cave, next to it  ::::::: where do you wish to go(enter the number in front of each path)")
