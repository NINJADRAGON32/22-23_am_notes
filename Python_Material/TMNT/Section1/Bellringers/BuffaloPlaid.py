from turtle import *
wn=Screen()
bTurds = []
rTurds = []
turdColors = ["black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red","black", "red"]
spacing = 0
i=0
horiz_spacing=-200
for color in turdColors:
    et = Turtle(shape = "square")
    et.color(turdColors.pop())
    # turds.append(et)
    if Turtle.color==("black"):
        bTurds.append(et)
    elif Turtle.color==("red"):
        rTurds.append(et)
    et.penup()
    et.goto(horiz_spacing,spacing)
    et.setheading(0)
    spacing+=20
    i+=1
    if i == 10 or 20 or 30 or 40 or 50 or 60 or 70 or 80:
        horiz_spacing+=20
for step in range (100):
    for t in bTurds:
        for t in rTurds:
            et.stamp()
            et.fd(50)
wn.mainloop()
