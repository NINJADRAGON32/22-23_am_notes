import turtle as t

turd = t.Turtle()
wn = t.Screen()




#functions
def drawSquare(d):
    for i in range(4):
        turd.forward(d)
        turd.right(90)
        
        
color = input("Enter a color (red,green,blue,orange,purple,white)")
size = int(input("how big of a square?(just need length"))
        
if color =="white":
    wn.bgcolor("black")

turd.pencolor(color)

#running code
drawSquare(size)
# turd.penup()
# turd.goto(100,100)
# turd.pendown()

drawSquare(d)

wn.mainloop()