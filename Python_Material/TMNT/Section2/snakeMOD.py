#---- import
import turtle as t
import time
import random as random
import winsound
#---- game config
speed=1.0
fontSetup=("Comic Sans",15,"normal")
delay=0.1
wn=t.Screen()
wn.bgcolor("gray")
wn.setup(width=600,height=600)

draw = t.Turtle()
draw.speed(0)
draw.pu()
draw.pensize(5)

p1 = t.Turtle(shape="square")
p1.speed(speed)
p1.pu()
p1.direction="stop"

p2 = t.Turtle(shape="square")
p2.color("green")
p2.speed(speed)
p2.pu()
p2.direction="stop"
p2.hideturtle()

food = t.Turtle()
food.speed(0)
food.shape("circle")
food.shapesize(.5,.5)
food.color("red")
food.pu()
food.goto(100,100)

bodyParts=[]
p2bodyParts=[]
#---- functions
def border():
    draw.goto(-300,-300)
    draw.pd()
    for i in range(4):
        draw.forward(600)
        draw.left(90)
    draw.pu()
def p1up():
    if p1.direction != "down":
        p1.direction = "up"
def p1left():
    if p1.direction != "right":
        p1.direction = "left"
def p1right():
    if p1.direction != "left":
        p1.direction = "right"
def p1down():
    if p1.direction !="up":
        p1.direction = "down"
        
def p2up():
    if p2.direction != "down":
        p2.direction = "up"
def p2left():
    if p2.direction != "right":
        p2.direction = "left"
def p2right():
    if p2.direction != "left":
        p2.direction = "right"
def p2down():
    if p2.direction !="up":
        p2.direction = "down"
        
def move():
    if p1.direction == "up":
        p1.sety(p1.ycor()+20)
    elif p1.direction == "down":
        p1.sety(p1.ycor()-20)
    elif p1.direction== "right":
        p1.setx(p1.xcor()+20)
    elif p1.direction == "left":
        p1.setx(p1.xcor()-20)
        
def move2():
    if p2.direction == "up":
        p2.sety(p2.ycor()+20)
    elif p2.direction == "down":
        p2.sety(p2.ycor()-20)
    elif p2.direction== "right":
        p2.setx(p2.xcor()+20)
    elif p2.direction == "left":
        p2.setx(p2.xcor()-20)
        
def p1hideTheBodyParts():
    global bodyParts
    winsound.Beep(500,1000)
    p1.goto(0,0)
    p1.direction = "stop"
    for  eachPart in bodyParts:
        eachPart.goto(1000,1000)
    bodyParts=[]
    
def p2hideTheBodyParts():
    global p2bodyParts
    winsound.Beep(500,1000)
    p2.goto(0,0)
    p2.direction = "stop"
    for  eachPart in p2bodyParts:
        eachPart.goto(1000,1000)
    p2bodyParts=[]

def PVP():
    global speed
    p2.showturtle()
    while True:
        wn.update()
        #TODO: Border Collision
        if p1.xcor() > 290 or p1.xcor() <-290 or p1.ycor()>290 or p1.ycor()<-290:
            p1hideTheBodyParts()
        # TODO: collide with food
        if p1.distance(food) < 20:
            #speed increases
            speed-=0.2
            #food moves
            food.goto(random.randint(-280,280),random.randint(-280,280))
            #grow a body part
            part = t.Turtle(shape="square")
            part.speed(0)
            part.pu()
            bodyParts.append(part)
        #Move the body parts
        #move the butt to the neck
        for i in range(len(bodyParts)-1,0,-1):
            x=bodyParts[i-1].xcor()
            y=bodyParts[i-1].ycor()
            bodyParts[i].goto(x,y)
        #move the neck to the p1
        if len(bodyParts)>0:
            x=p1.xcor()
            y=p1.ycor()
            bodyParts[0].goto(x,y)
        move()
        for part in bodyParts:
            if part.distance(p1)<10:
                p1hideTheBodyParts()
            elif part.distance(p2)<10:
                p2hideTheBodyParts()
    # this is the start of the player 2 physics
        if p2.xcor() > 290 or p2.xcor() <-290 or p2.ycor()>290 or p2.ycor()<-290:
            p2hideTheBodyParts()
        if p2.distance(food) < 20:
            #speed increases
            speed-=0.2
            #food moves
            food.goto(random.randint(-280,280),random.randint(-280,280))
            #grow a body part
            p2part = t.Turtle(shape="square")
            p2part.color("green")
            p2part.speed(0)
            p2part.pu()
            p2bodyParts.append(p2part)
        for i in range(len(p2bodyParts)-1,0,-1):
            x=p2bodyParts[i-1].xcor()
            y=p2bodyParts[i-1].ycor()
            p2bodyParts[i].goto(x,y)
        if len(p2bodyParts)>0:
            x=p2.xcor()
            y=p2.ycor()
            p2bodyParts[0].goto(x,y)
        move2()
        for p2part in p2bodyParts:
            if p2part.distance(p2)<10:
                p2hideTheBodyParts()
            elif p2part.distance(p1)<10:
                p1hideTheBodyParts()
                
        time.sleep(delay)

def normal():
    global speed
    while True:
        wn.update()
        
        #TODO: Border Collision
        if p1.xcor() > 290 or p1.xcor() <-290 or p1.ycor()>290 or p1.ycor()<-290:
            p1hideTheBodyParts()
                
        # TODO: collide with food
        if p1.distance(food) < 20:
            #speed increases
            speed-=0.2
            #food moves
            food.goto(random.randint(-280,280),random.randint(-280,280)) 
            #grow a body part
            part = t.Turtle(shape="square")
            part.speed(0)
            part.pu()
            bodyParts.append(part)
        #Move the body parts
        #move the butt to the neck
        for i in range(len(bodyParts)-1,0,-1):
            x=bodyParts[i-1].xcor()
            y=bodyParts[i-1].ycor()
            bodyParts[i].goto(x,y) 
        #move the neck to the p1
        if len(bodyParts)>0:
            x=p1.xcor()
            y=p1.ycor()
            bodyParts[0].goto(x,y) 
        
        
        move()
        
        for part in bodyParts:
            if part.distance(p1)<10:
                p1hideTheBodyParts()
        
        
        
        time.sleep(delay)

#---- events
wn.onkeypress(p1up,"w")
wn.onkeypress(p1down, "s")
wn.onkeypress(p1left, "a")
wn.onkeypress(p1right, "d")
wn.onkeypress(p2up,"Up")
wn.onkeypress(p2down, "Down")
wn.onkeypress(p2left, "Left")
wn.onkeypress(p2right, "Right")
wn.onkeypress(PVP, "p")
wn.onkeypress(normal, "n")
wn.listen()
#---- mainloop
border()
draw.goto (-300,310)
draw.write(" To play PVP press (p) to play Normal snake press(n)", font=fontSetup)
draw.goto(-50,-320)
draw.write(" controls:",font=fontSetup)
draw.goto(-200,-340)
draw.write("player 1: W,A,S,D          player 2: use arrows",font=fontSetup)


wn.mainloop()