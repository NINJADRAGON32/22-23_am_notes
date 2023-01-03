#   a123_apple_1.py
import turtle as trtl

#-----setup-----
pear_image = "pear.gif"
apple_image = "apple.gif" # Store the file name of your shape
ground_height = -200

wn = trtl.Screen()
# wn.setup(width=1.0, height=1.0)
wn.addshape(pear_image)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

apple = trtl.Turtle()
apple.penup()
pear = trtl.Turtle()
pear.penup()
pear.goto(100,100)
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def draw_pear(active_pear):
  active_pear.shape(pear_image)
  wn.update()

def dropApple():
  apple.goto(apple.xcor(),ground_height)
  
def dropPear():
  pear.goto(pear.xcor(),ground_height)
#-----function calls-----
draw_apple(apple)
draw_pear(pear)
#window.onkeypress(command,binding)
wn.onkeypress(dropApple,"a")
wn.onkeypress(dropPear, "p")

wn.listen()
wn.mainloop()