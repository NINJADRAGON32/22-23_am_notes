import turtle as t
wn = t.Screen()
ap = t.Turtle()
def asphalt():
    ap.penup()
    ap.speed(0)
    ap.goto(100,200)
    ap.color("grey")
    ap.setheading(270)
    ap.fillcolor("grey")
    ap.begin_fill()
    ap.forward(400)
    ap.setheading(180)
    ap.forward(100)
    ap.setheading(90)
    ap.forward(200)
    ap.setheading(0)
    ap.forward(100)
    ap.end_fill()

asphalt()






wn.mainloop()