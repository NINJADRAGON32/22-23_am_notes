#CSE challenges 1

# this is the start of the first challenge for determining of you passed or not

def problem1():
    score = (int(input("enter your score: ")))
    if score >= 60:
        print("you passed")
    elif score < 60 and score >= 0:
        print("you failed")
    else:
        print("invalid input")

# this is the start of the second challenge
    
def problem2():
    max = 0
    min = 100000
    number = 0
    while number != -1:
        number = int(input("enter positive numbers and when you wish to   stop enter -1: "))
    #this is not a complex if statement so it does the check for both max and min
    if number >= max:
        max = number 
    if number <= min and number >= 0:
        min = number
    if number <= -2:
        print("invalid input")
    print(f"max:",{max})
    print(f"min:",{min})

# this is the start of problem 3

def problem3():    
    import math
    x1 = int(input("enter the first X cord. here: "))
    y1 = int(input("enter the first Y cord. here: "))
    print(f"first cordinates: ",{x1},",",{y1})
    x2 = int(input("enter the second X cord. here: "))
    y2 = int(input("enter the second Y cord. here: "))
    print(f"second cordinates: ",{x2},",",{y2})
    a=x1-x2 
    b=y1-y2
    c = (a*a)+(b*b)
    math.sqrt(c)
    print(f"distance: ",{c})

# this is the start of problem 4

def problem4():
    import random
    number = random.randint(1, 14)
    suit = random.randint(1, 4)

    # labeling face cards
    if number == (1):
        number = "Ace"
    elif number == (11):
        NUMBER = "Jack"
    elif number ==(12):
        number = "Queen"
    elif number == (13):
        number = "King"

    # Matching numbers to colors
    if suit == (1):
        suit = "hearts"
    elif suit == (2):
        suit = "diamonds"
    elif suit == (3):
        suit = "spades"
    elif suit == (4):
        suit = "clubs"

    print(f"you drew the",{number},"of",{suit},)

UI=input("what challenge would you like to test: (problem1),(problem2),(problem3), or (problem4) (press q to quit)")

while UI != "q":
    if UI == "problem1":
        problem1()
    elif UI == "problem2":
        problem2()
    elif UI == "problem3":
        problem3()
    elif UI == "problem4":
        problem4()
    UI=input("what challenge would you like to test: (problem1),(problem2),(problem3), or (problem4) (press q to quit)")



