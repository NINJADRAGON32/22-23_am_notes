#import module aliasName t
import turtle as t

turd = t.Turtle()
turd2 = t.Turtle()
wn = t.Screen() #screen for turtle
turd.shape("turtle")
turd.speed('fastest')

while True:
    turd.speed(0)
    turd.forward(100)
    turd.right(135)

#that must always go at the end
wn.mainloop()