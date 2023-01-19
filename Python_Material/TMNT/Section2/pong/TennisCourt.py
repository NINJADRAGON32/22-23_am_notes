#---- imports
import turtle as t

#---- global variables
wn=t.Screen()
court_width=1000
court_Height=600
border = t.Turtle()#visible=False)
wl = t.Turtle()

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
    
def vertWhiteLines(x,y):
    wl.showturtle()
    wl.speed(0)
    wl.color("black")
    wl.pu()
    wl.goto(x,y)
    wl.setheading(270)
    for i in range(40):
        wl.pd()
        wl.forward(5)
        wl.pu()
        wl.forward(10)
 
    wl.hideturtle()
#---- events

#---- main loop
vertWhiteLines(0,court_Height/2)
drawField()
wn.mainloop()