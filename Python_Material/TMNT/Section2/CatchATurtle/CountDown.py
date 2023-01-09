import turtle as t

wn=t.Screen()
timer=10
fontSetup=("Comic Sans",30,"normal")
interval=1000


timeKeeper=t.Turtle()
timeKeeper.penup()
timeKeeper.hideturtle()
timeKeeper.goto(-100,200)
timeKeeper.pd()
timeKeeper.speed(0)

#functions
def updatetimer():
    global timer
    timeKeeper.clear()
    if timer<=0:
        timeKeeper.write("Times Up!",font=fontSetup)
    else:
        timer-=1
        timeKeeper.write(f"Timer: {timer}",font=fontSetup)
        timeKeeper.getscreen().ontimer(updatetimer,interval)

#event
wn.ontimer(updatetimer,interval)


wn.mainloop()