#   a115_robot_maze.py
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

def moveUp():
  robot.setheading(90)
  robot.forward(50)
  
def moveDown():
  robot.setheading(270)
  robot.forward(50)
  
def moveLeft():
  robot.setheading(180)
  robot.forward(50)
  
def moveRight():
  robot.setheading(0)
  robot.forward(50)

def home():
  robot.goto(0,0)
  
#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()
turdXChor=robot.xcor()
turdYChor=robot.ycor()
turdCor=robot.pos()
#---- TODO: change maze here
wn.bgpic("maze1.png") # other file names should be maze2.png, maze3.png

# while True:
  

#---- TODO: begin robot movement here
trtl.onkey(moveUp, "w")
trtl.onkey(moveLeft, "a")
trtl.onkey(moveRight, "d")
trtl.onkey(moveDown, "s")
trtl.onkey(home, "h")

#---- navigation for maze 1
def maze1():
  wn.bgpic("maze1.png")
  robot.goto(-100,-100)
  for i in range(4):
    moveUp()
  for i in range (4):
    moveRight()
  
#---- navigation for maze 2
def maze2():
  robot.goto(-100,-100)
  wn.bgpic("maze2.png")
  for i in range(3):
    moveUp()
  for i in range(2):
    moveRight()

#---- navigation for maze 3
def maze3():
  robot.goto(-100,-100)
  wn.bgpic("maze3.png")
  for i in range (4):
    moveUp()
    moveRight()

#---- calling functions
trtl.onkey(maze1, "b")
trtl.onkey(maze2, "n")
trtl.onkey(maze3, "m")
#---- end robot movement 
wn.listen()
wn.mainloop()
