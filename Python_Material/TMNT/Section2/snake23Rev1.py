#---- import
import turtle as t
import time 
import random as random
#---- game config
delay=0.1

wn=t.Screen()
wn.bgcolor("gray")
wn.setup(width=600,height=600)

head = t.Turtle(shape="square")
head.speed(0)
head.pu()
head.direction="stop"

food = t.Turtle()
food.speed(0)
food.shape("circle")
food.shapesize(.5,.5)
food.color("red")
food.pu()
food.goto(100,100)

bodyParts=[]
#---- functions
def up():
    if head.direction != "down":
        head.direction = "up"
        
def left():
    if head.direction != "right":
        head.direction = "left"
        
def right():
    if head.direction != "left":
        head.direction = "right"
        
def down():
    if head.direction !="up":
        head.direction = "down"

def move():
    if head.direction == "up":
        head.sety(head.ycor()+20)
    elif head.direction == "down":
        head.sety(head.ycor()-20)
    elif head.direction== "right":
        head.setx(head.xcor()+20)
    elif head.direction == "left":
        head.setx(head.xcor()-20)
        
def hideTheBodyParts():
    global bodyParts
    head.goto(0,0)
    head.direction = "stop"
    for  eachPart in bodyParts:
        eachPart.goto(1000,1000) 
    bodyParts=[]
    
#---- events
wn.onkeypress(up,"w")
wn.onkeypress(down, "s")
wn.onkeypress(left, "a")
wn.onkeypress(right, "d")
wn.listen()
#---- mainloop
while True:
    wn.update()
    
    #TODO: Border Collision
    if head.xcor() > 290 or head.xcor() <-290 or head.ycor()>290 or head.ycor()<-290:
       hideTheBodyParts()
             
    # TODO: collide with food
    if head.distance(food) < 20:
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
    #move the neck to the head
    if len(bodyParts)>0:
        x=head.xcor()
        y=head.ycor()
        bodyParts[0].goto(x,y) 
    
    
    move()
    
    for part in bodyParts:
        if part.distance(head)<10:
            hideTheBodyParts()
    
    
    
    time.sleep(delay)

