#---- import
import turtle as t
import time
import random as random
#---- game config
delay=0.1

wn=t.Screen()
wn.bgcolor("gray")
wn.setup(width=600,height=600)

p1 = t.Turtle(shape="square")
p1.speed(0)
p1.pu()
p1.direction="stop"
p2 = t.Turtle(shape="square")
p2.color("green")
p2.speed(0)
p2.pu()
p2.direction="stop"

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
        p2.sety(p1.ycor()+20)
    elif p2.direction == "down":
        p2.sety(p1.ycor()-20)
    elif p2.direction== "right":
        p2.setx(p1.xcor()+20)
    elif p2.direction == "left":
        p2.setx(p1.xcor()-20)
        
def p1hideTheBodyParts():
    global bodyParts
    p1.goto(0,0)
    p1.direction = "stop"
    for  eachPart in bodyParts:
        eachPart.goto(1000,1000)
    bodyParts=[]
    
def p2hideTheBodyParts():
    global p2bodyParts
    p2.goto(0,0)
    p2.direction = "stop"
    for  eachPart in p2bodyParts:
        eachPart.goto(1000,1000)
        
#---- events
wn.onkeypress(p1up,"w")
wn.onkeypress(p1down, "s")
wn.onkeypress(p1left, "a")
wn.onkeypress(p1right, "d")
wn.onkeypress(p2up,"Up")
wn.onkeypress(p2down, "Down")
wn.onkeypress(p2left, "Left")
wn.onkeypress(p2right, "Right")
wn.listen()
#---- mainloop
while True:
    wn.update()
    #TODO: Border Collision
    if p1.xcor() > 290 or p1.xcor() <-290 or p1.ycor()>290 or p1.ycor()<-290:
       p1hideTheBodyParts()
    if p2.xcor() > 290 or p2.xcor() <-290 or p2.ycor()>290 or p2.ycor()<-290:
       p2hideTheBodyParts()
    # TODO: collide with food
    if p1.distance(food) < 20:
        #food moves
        food.goto(random.randint(-280,280),random.randint(-280,280))
        #grow a body part
        part = t.Turtle(shape="square")
        part.speed(0)
        part.pu()
        bodyParts.append(part)
    if p2.distance(food) < 20:
        #food moves
        food.goto(random.randint(-280,280),random.randint(-280,280))
        #grow a body part
        p2part = t.Turtle(shape="square")
        p2.color("green")
        p2part.speed(0)
        p2part.pu()
        p2bodyParts.append(p2part)
    #Move the body parts
    #move the butt to the neck
    for i in range(len(bodyParts)-1,0,-1):
        x=bodyParts[i-1].xcor()
        y=bodyParts[i-1].ycor()
        bodyParts[i].goto(x,y)
    for i in range(len(p2bodyParts)-1,0,-1):
        x=p2bodyParts[i-1].xcor()
        y=p2bodyParts[i-1].ycor()
        p2bodyParts[i].goto(x,y)
    #move the neck to the p1
    if len(bodyParts)>0:
        x=p1.xcor()
        y=p1.ycor()
        bodyParts[0].goto(x,y)
    if len(p2bodyParts)>0:
        x=p2.xcor()
        y=p2.ycor()
        p2bodyParts[0].goto(x,y)
    move()
    move2()
    for part in bodyParts:
        if part.distance(p1)<10:
            p1hideTheBodyParts()
            
    for part in bodyParts:
        if part.distance(p1)<10:
            p2hideTheBodyParts()
            
    time.sleep(delay)
    