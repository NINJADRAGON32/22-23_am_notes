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

#---- initialize turtles
mazeDrawer = t.Turtle()
mazeDrawer.pensize(5)
mazeDrawer.pencolor("blue")
mazeDrawer.speed(0)

mazeRunner = t.Turtle()
mazeRunner.color("red")
mazeRunner.pu()
mazeRunner.goto(-pathWidth*2,pathWidth*2)
mazeRunner.pendown()

follow = t.Turtle()
follow.color("grey")
follow.speed(1)

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
    margin=1
    items = canvas.find_overlapping(x+margin, -y+margin, x-margin, -y+margin)
    #if the items variable has overlap
    if(len(items)>0): #stack of what is overlapping
        canvasColor= canvas.itemcget(items[0], "fill")
        if canvasColor=="blue":
            mazeRunner.color("gray")
            wn.onkeypress(None,"Return")
            return                      #shortcut to stop the function
    wn.ontimer(go,50)
    wn.ontimer(followRunner,50)
    
def followRunner():
    follow.setheading(follow.towards(mazeRunner))
    follow.forward(1)
    
#---- events
wn.onkeypress(moveUp, "w")
wn.onkeypress(moveDown, "s")
wn.onkeypress(moveLeft, "a")
wn.onkeypress(moveRight, "d")
wn.onkeypress(go, "Return") #enter nd return are different


    

#---- main loop

drawMaze()

wn.listen()
wn.mainloop()
