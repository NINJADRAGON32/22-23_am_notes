import turtle as t

########## drawing the intersection ###########
#---- Turtles
wn = t.Screen()
ap = t.Turtle()
yl = t.Turtle()
wl = t.Turtle()

#---- Functions
def asphalt():
    ap.penup()
    ap.speed(0)
    ap.goto(-100,300)
    ap.color("grey")
    ap.setheading(0)
    ap.fillcolor("grey")
    ap.begin_fill()
    ap.forward(200)
    ap.setheading(270)
    ap.forward(600)
    ap.setheading(180)
    ap.forward(200)
    ap.setheading(90)
    ap.forward(600)
    ap.end_fill()
    ap.goto(-300,100)
    ap.color("grey")
    ap.setheading(0)
    ap.fillcolor("grey")
    ap.begin_fill()
    ap.forward(600)
    ap.setheading(270)
    ap.forward(200)
    ap.setheading(180)
    ap.forward(600)
    ap.setheading(90)
    ap.forward(200)
    ap.end_fill()
    ap.hideturtle()
    
def yellowLines():
    yl.penup
    yl.speed(0)
    yl.goto(-300,0)
    yl.color("yellow")
    yl.setheading(0)
    yl.pendown()
    yl.forward(200)
    yl.penup()
    yl.forward(200)
    yl.pendown()
    yl.forward(200)
    yl.pu()
    yl.goto(0,300)
    yl.setheading(270)
    yl.pendown()
    yl.forward(200)
    yl.penup()
    yl.forward(200)
    yl.pendown()
    yl.forward(200)
    yl.hideturtle()
    
def vertWhiteLines():
    wl.showturtle()
    wl.speed(0)
    wl.color("white")
    wl.pu()
    wl.goto(x,y)
    wl.setheading(270)
    for i in range(14):
        wl.pd()
        wl.forward(5)
        wl.pu()
        wl.forward(10)
 
    wl.hideturtle()

def horWhiteLine():
    wl.showturtle()
    wl.speed(0)
    wl.color("White")
    wl.pu()
    wl.goto(x,y)
    wl.setheading(0)
    for i in range(14):
        wl.pd()
        wl.forward(5)
        wl.pu()
        wl.forward(10)
    wl.hideturtle()

#---- calling functions
asphalt()
yellowLines()
x,y=-50,300
vertWhiteLines()
x,y=50,300
vertWhiteLines()
x,y=-50,-100
vertWhiteLines()
x,y=50,-100
vertWhiteLines()
x,y=-300,50
horWhiteLine()
x,y=-300,-50
horWhiteLine()
x,y=100,50
horWhiteLine()
x,y=100,-50
horWhiteLine()

################################################

#collision for turtles
horizontalTurts = []
verticalTurts = []
# use interesting shapes and colors
turtleShapes = ["arrow", "turtle", "circle", "square"]#, "triangle", "classic"]
horizColors = ["red", "blue", "green", "orange"]#, "purple", "gold"]
vertColors = ["darkred", "darkblue", "lime", "salmon"]#, "indigo", "brown"]
spacing=-75
for shape in turtleShapes:
    ht = t.Turtle(shape=shape)
    horizontalTurts.append(ht)
    ht.penup()
    ht.fillcolor(horizColors.pop())
    ht.goto(-300,spacing)
    ht.setheading(0)
    vt = t.Turtle(shape=shape)
    verticalTurts.append(vt)
    vt.penup()
    vt.fillcolor(vertColors.pop())
    vt.goto(-spacing,300)
    vt.setheading(270)
    spacing+=50
#moving the turtles
distanceToMove=2
collisonDistance=5
for step in range(100):
    for h in horizontalTurts:
        for v in verticalTurts:
            h.fd(distanceToMove)
            v.fd(distanceToMove)
        #check for collision
        if h.xcor==300:
            h.goto(-300,spacing)
        elif (abs(h.xcor() - v.xcor()) < collisonDistance):
            if (abs(h.ycor()-v.ycor())< collisonDistance):
                h.color("red")
                v.color("red")
                h.stamp()
                v.stamp()
                h.hideturtle()
                v.hideturtle()
                horizontalTurts.remove(h)       #remove from the list stop stop them moving, cant move something not in the list
                verticalTurts.remove(v) 
        



wn.mainloop()