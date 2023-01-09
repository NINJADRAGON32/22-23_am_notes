import turtle as t

wn=t.Screen()
score=0
fontSetup=("Comic Sans",30,"normal")

scoreKeeper=t.Turtle()
scoreKeeper.penup()
scoreKeeper.hideturtle()
scoreKeeper.goto(100,200)
scoreKeeper.pd()
scoreKeeper.speed(0)

#functions
def updateScore(x,y):
    global score
    score+=1
    scoreKeeper.clear()
    scoreKeeper.write(f"Score: {score}",font=fontSetup)


#event
wn.onscreenclick(updateScore)


wn.mainloop()



