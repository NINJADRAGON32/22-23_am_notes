import turtle as t
import random as r

tree = t.Turtle()
presents=[]
wn = t.Screen()
wn.bgcolor('black')

#def tree

def presents(numberOfPresents,colorOfPresents):
    
    for i in range(numberOfPresents):
        p=t.turtle()
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
snow(500,'white',-(wn.window_width()),(wn.window_width()),600,-300,30,5,300)



wn.mainloop()