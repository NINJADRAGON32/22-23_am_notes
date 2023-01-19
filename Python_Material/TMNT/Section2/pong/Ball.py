#---- imports
import turtle as t
import random as r
#---- global variables
wn=t.Screen()
court_width=1000
court_Height=600
paddle_width=50
fontSettings = ("Arial",80,"normal")
leftScore=0
rightScore=0
#---- turtles
border = t.Turtle()#visible=False)
border.color("white")
wn.bgcolor("black")
wl = t.Turtle()

ball = t.Turtle()
ball_Size=15
ball.shape("circle")
ball.color("white")
ball.pu()
ball.speed(0)

lP = t.Turtle("square")
lP.pu()
lP.color("red")
lP.speed(0)
lP.setx(-court_width/2)
lP.turtlesize(4,1)

rP = t.Turtle("square")
rP.pu()
rP.color("blue")
rP.speed(0)
rP.setx(court_width/2)
rP.turtlesize(4,1)

lScore = t.Turtle(visible=False)
lScore.color("white")
lScore.speed(0)
lScore.penup()
lScore.setposition(-court_width/4,court_Height/4)
lScore.write(leftScore,font=fontSettings)

rScore = t.Turtle(visible=False)
rScore.color("white")
rScore.speed(0)
rScore.penup()
rScore.setposition(court_width/4,court_Height/4)
rScore.write(rightScore,font=fontSettings)
#---- functions
def drawField():
    border.speed(0)
    border.pensize(3)
    border.pu()
    border.goto(-court_width/2,court_Height/2)
    border.pd()
    border.setheading(0)
    border.goto(court_width/2,court_Height/2)
    border.pu()
    border.goto(-court_width/2,-court_Height/2)
    border.pd()
    border.goto(court_width/2,-court_Height/2)
    wl.showturtle()
    wl.speed(0)
    wl.color("white")
    wl.pu()
    wl.goto(0,court_Height/2)
    wl.setheading(270)
    for i in range(40):
        wl.pd()
        wl.forward(5)
        wl.pu()
        wl.forward(10)
 
    wl.hideturtle()

def moveBall():
    global leftScore,rightScore
    ball.fd(20)
    x,y = ball.pos()
    # bounce off the top or bottom wall
    if y >= (court_Height/2-ball_Size)or y<(-court_Height/2+ball_Size): 
        ball.setheading(ball.heading()+r.randint(25,75))
    elif x >= (court_width/2-ball_Size)or x<(-court_width/2+ball_Size): 
        if x>court_width/2:
            leftScore+=1
            lScore.clear()
            lScore.write(leftScore,font=fontSettings)
        elif x<-court_width/2:
            rightScore+=1
            rScore.clear()
            rScore.write(rightScore,font=fontSettings)
        resetBall()
    else:
        collideWithPaddle(lP,ball)
        collideWithPaddle(rP, ball)
        
    wn.ontimer(moveBall,20)
def resetBall():
    ball.setpos(0,0)
    if r.randint(0,1)==0:
        ball.setheading(r.randint(150,210))
    else:
        ball.setheading(r.randint(-30,30))

def UpLeft():
    if lP.ycor()< (court_Height/2-paddle_width):
        lP.sety(lP.ycor()+20)
def DownLeft():
    if lP.ycor()> (-court_Height/2+paddle_width):
        lP.sety(lP.ycor()-20)
        
def UpRight():
    if rP.ycor()< (court_Height/2-paddle_width):
        rP.sety(rP.ycor()+20)
def DownRight():
    if rP.ycor()> (-court_Height/2+paddle_width):
        rP.sety(rP.ycor()-20)

def collideWithPaddle(paddle,b):
    if paddle.distance(b) <paddle_width:
        b.setheading(180-b.heading())
        if b.xcor()>0:
            b.setx(b.xcor()-5)
        else:
            b.setx(b.xcor()+5)
        b.fd(10)
#---- events
wn.onkeypress(resetBall,"h")
wn.onkeypress(UpLeft, "w")
wn.onkeypress(DownLeft, "s")
wn.onkeypress(UpRight, "Up")
wn.onkeypress(DownRight, "Down")
wn.listen()
#---- main loop
drawField()

moveBall()

wn.mainloop()