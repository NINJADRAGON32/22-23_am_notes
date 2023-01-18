#---- import 
import turtle as t
import random as r
import leaderboard as lb 
#---- Global Variables
wn=t.Screen()     
fontSetup=("Comic Sans",30,"normal")
interval=1000
score=0
FILENAME="Database.txt"
timer=25
begin=0

#---- initialize turtles
bob = t.Turtle()
bob.shape("turtle")
bob.shapesize(2)
bob.fillcolor("purple")
bob.speed(0)
bob.penup()

timeKeeper=t.Turtle()
timeKeeper.penup()
timeKeeper.hideturtle()
timeKeeper.goto(-100,300)
timeKeeper.pd()
timeKeeper.speed(0)

scoreKeeper=t.Turtle()
scoreKeeper.penup()
scoreKeeper.hideturtle()
scoreKeeper.goto(100,300)
scoreKeeper.pd()
scoreKeeper.speed(0)

#---- functions
def bobClicked(x,y):
    print("bob clicked")
    print(x,y)
    bob.color("red","white")
    bob.stamp()
    bob.color("purple")
    moveBob()
    
    #updating the score
    global score
    score+=1
    scoreKeeper.clear()
    scoreKeeper.write(f"Score: {score}",font=fontSetup)
    
def moveBob():
    t.Screen().bgcolor("red")
    newX=r.randint(-300,300)
    newY=r.randint(-300,300)
    bob.goto(newX,newY)
    t.Screen().bgcolor("white")
    
def updatetimer():
    global timer
    timeKeeper.clear()
    if timer<=0:
        timeKeeper.write("Times Up!",font=fontSetup)
        bob.hideturtle()
        manageLeaderBoard()
    else:
        timer-=1
        timeKeeper.write(f"Timer: {timer}",font=fontSetup)
        timeKeeper.getscreen().ontimer(updatetimer,interval)

def updateScore(x,y):
    global score
    score+=1
    scoreKeeper.clear()
    scoreKeeper.write(f"Score: {score}",font=fontSetup)

def manageLeaderBoard():
    global score
    #get datat from text file
    namesList=lb.getNames(FILENAME)
    scoresList=lb.getScores(FILENAME)
    
    #check to see if you made the laderboard
    
    #check to update leaderBoard
    if(int(len(scoresList))<4 or int(score)>=int(scoresList[-1])):
        name=input("congrats ur on the board name pls \n\t: ")
        lb.updateLeaderBoard(FILENAME,namesList,scoresList,name,15)
    else:
        print("did not make leaderboard")
    #display leaderBoard
    lb.draw_leaderboard(False, namesList, scoresList, scoreKeeper, 10)

#---- events
bob.onclick(bobClicked)
wn.ontimer(updatetimer,interval)

#---- main loop

wn.mainloop()


'''
    1. Click the turtle
    2. move the turtle
    3. Update a score
    4. Countdown
'''