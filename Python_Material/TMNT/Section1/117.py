import turtle as t

#global
myTurts = []
tShapes = ["classic","turtle","square","circle","triangle","arrow"]*7
tColors = ["red","blue","green","sienna","cyan","purple"]*7
#turtles
for i in range(len(tShapes)):
    mikey=t.Turtle(shape=tShapes[i])
    mikey.color(tColors[i])
    mikey.penup()
    mikey.speed(0)
    myTurts.append(mikey)


#run 

startx,starty,direction,grow=0,0,90,0

for turt in myTurts:
    turt.goto(startx,starty)
    turt.setheading(direction)
    turt.pendown()
    turt.right(45)
    turt.forward(5+grow)
    direction=turt.heading()

    startx=turt.xcor()
    starty=turt.ycor()
    grow+=5

# #follow the leader
# while True:
#     for i in range(len(myTurts)-1):
#         nextX,nextY= myTurts[i+1].xcor(),myTurts[i+1].ycor()
#         myTurts[i].goto(nextX.nextY)

wn = t.Screen()
wn.mainloop()

