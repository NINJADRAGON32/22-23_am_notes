#---- powershelll config
#cd .\Documents\22-23_am_notes\Python_Material\TMNT\Section2\MazeRunner\

#---- imports
import turtle as t
import random as r

#---- global variables
wn=t.Screen()
wallLength=15
numberOfWalls=25
pathWidth=15
barrier=15
wallsMade=0
timer=0
fontSetup=("Comic Sans",30,"normal")
interval=1000
p=False
#---- initialize turtles
mazeDrawer = t.Turtle()
mazeDrawer.pensize(5)
mazeDrawer.pencolor("blue")
mazeDrawer.speed(0)

mazeRunner = t.Turtle()
mazeRunner.color("red")
mazeRunner.pu()
mazeRunner.goto(-pathWidth*2,pathWidth*2)

timeKeeper=t.Turtle()
timeKeeper.penup()
timeKeeper.hideturtle()
timeKeeper.goto(-100,300)
timeKeeper.pd()
timeKeeper.speed(0)

follow = t.Turtle()
follow.color("blue")
follow.speed(0.99)
follow.pu()

#---- functions
def drawDoor(pos):
    mazeDrawer.fd(pos)
    mazeDrawer.penup()
    mazeDrawer.fd(pathWidth*2)
    mazeDrawer.pd()
    
def drawBarrier(pos):
    mazeDrawer.fd(pos)
    mazeDrawer.left(90)
    mazeDrawer.fd(pathWidth*2)
    mazeDrawer.fd(-pathWidth*2)
    mazeDrawer.right(90)

def drawMaze():
    wallLength=15
    for w in range(numberOfWalls): 
        wallLength+=pathWidth
        if w >4:
            mazeDrawer.left(90)
            
            #where do we draw the door and the barriers inside of a walll length
            doorSpot=r.randint(pathWidth*2,(wallLength-2*pathWidth))
            barrierSpot=r.randint(pathWidth*2,(wallLength-2*pathWidth))
            
            #check to make sure a door and barrier do not render on top of each other
            while abs(doorSpot-barrierSpot)< pathWidth:
                doorSpot=r.randint(pathWidth*2,(wallLength-2*pathWidth))
            #draw the wall
            if(doorSpot<barrierSpot):
                drawDoor(doorSpot)
                drawBarrier(barrierSpot-doorSpot-pathWidth*2)
                mazeDrawer.fd(wallLength-barrierSpot)
            else: 
                drawBarrier(barrierSpot)
                drawDoor(doorSpot-barrierSpot)
                mazeDrawer.fd(wallLength-doorSpot-pathWidth*2)
        # elif w>=(numberOfWalls-1):
        #     mazeDrawer.left(90)
        #     doorSpot=r.randint(pathWidth*2,(wallLength-2*pathWidth))
        #     drawDoor(doorSpot)
        #     drawBarrier(barrierSpot-doorSpot-pathWidth*2)
        #     mazeDrawer.fd(wallLength-barrierSpot)
    for i in range(4):
        wallLength+=pathWidth
        mazeDrawer.left(90)
        mazeDrawer.fd(wallLength)
    mazeDrawer.hideturtle()

def moveUp():
  mazeRunner.setheading(90)
  
def moveDown():
  mazeRunner.setheading(270)
  
def moveLeft():
  mazeRunner.setheading(180)
  
def moveRight():
  mazeRunner.setheading(0)

def go():
    mazeRunner.fd(2)
    canvas = wn.getcanvas()
    x,y=mazeRunner.pos()
    margin=2
    items = canvas.find_overlapping(x+margin, -y+margin, x-margin, -y+margin)
    #if the items variable has overlap
    if(len(items)>0): #stack of what is overlapping
        canvasColor= canvas.itemcget(items[0], "fill")
        if canvasColor=="blue":
            resetGame()
                                  #shortcut to stop the function
    wn.ontimer(go,50)
    wn.ontimer(followRunner,50)
   
# def pause():
#     p=True
#     while p==True:
#         wn.onkeypress(resume, "m") 
#         pass

# def resume():
#     p=False
            
def followRunner():
    follow.setheading(follow.towards(mazeRunner))
    follow.forward(1) 

def resetGame():
    mazeRunner.color("red")
    mazeRunner.pu()
    mazeRunner.goto(-pathWidth*2,pathWidth*2)

def updatetimer():
    global timer
    timeKeeper.clear()
    timer+=1
    timeKeeper.write(f"Timer: {timer}",font=fontSetup)
    timeKeeper.getscreen().ontimer(updatetimer,interval)
    
#---- events
wn.onkeypress(moveUp, "w")
wn.onkeypress(moveDown, "s")
wn.onkeypress(moveLeft, "a")
wn.onkeypress(moveRight, "d")
wn.onkeypress(resetGame, "r")
wn.onkeypress(go, "Return") #enter and return are different
wn.ontimer(updatetimer,1000)
# wn.onkeypress(pause, "p")

#---- main loop

drawMaze()

wn.listen()
wn.mainloop()
