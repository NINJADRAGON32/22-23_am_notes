import turtle as t
import random as r

tree = t.Turtle()
presents=[]
wn = t.Screen()
wn.bgcolor('black')

#def tree

def snowMan():
     man =t.Turtle()
     man.speed(0)
     man.color('white')
     man.penup()
     man.goto(-850,-375)
     man.pendown()
     man.fillcolor('white')
     man.begin_fill()
     man.circle(50)
     man.end_fill() 
     man.begin_fill()
     man.left(90)
     man.forward(75)
     man.right(90)
     man.circle(40)
     man.end_fill() 
     man.left(90)
     man.forward(65)
     man.right(90)
     man.begin_fill()
     man.circle(30)
     man.end_fill() 
     #eyes
     man.color('black')
     man.penup()
     

def window():
     window = t.Turtle()
     window.color('white')
     window.penup()
     window.speed(0)
     window.goto(-400,-250)
     window.pendown()
     window.fillcolor('white')
     window.begin_fill()
     for i in range(4):
          window.forward(800)
          window.left(90)
     window.end_fill()
     window.forward(50)
     window.left(90)
     window.forward(50)
     window.right(90)
     window.color('black')
     window.fillcolor('tan')
     window.begin_fill()
     for i in range(4):
          window.forward(700)
          window.left(90)
     window.end_fill()
     window.forward(350)
     window.color('white')
     window.pensize(5)
     window.left(90)
     window.forward(700)
     window.left(180)
     window.forward(350)
     window.pensize(10)
     window.left(90)
     window.forward(350)
     window.left(180)
     window.forward(700)
     window.hideturtle()


def ground(numberOfBushes):
     ground = t.Turtle()
     ground.speed(0)
     ground.fillcolor('green')
     ground.penup()
     ground.goto(-1000,-350)
     ground.pendown
     for i in range (numberOfBushes):
          ground.begin_fill()
          for i in range (4):
               ground.forward(450)
               ground.right(90)
          ground.end_fill()
          ground.forward(500) 
            
     
def presents(numberOfPresents,colorOfPresents):
    
    for i in range(numberOfPresents):
        p=t.Turtle()
        p.color(colorOfPresents)
        p.speed(0)
        p.penup()
        p.goto
        

def snow(numberOfFlakes,colorOfSnow,farLeft,farRight,upper,lower,speed,variation,ground):
     snowFlakes=[]
     for i in range(numberOfFlakes):
          s=t.Turtle(shape='circle')
          s.color(colorOfSnow)
          s.speed(0)
          s.penup()
          s.goto(r.randint(farLeft,farRight),r.randint(lower,upper))        #r->random module
          snowFlakes.append(s)

     #runningcode
     while True:
          for s in snowFlakes:
               newX=s.xcor()+r.randint(-variation, variation)
               newY=s.ycor()+r.randint(-speed, 0)
               s.goto(newX,newY)
               if s.ycor()<-ground:
                    s.stamp()
                    s.sety(r.randint(lower,upper))





#calling the functions

window()
presents(1,'red')
ground(4)
snowMan()
snow(300,'white',-1000,1000,600,250,100,5,r.randint(325,350))





wn.mainloop()