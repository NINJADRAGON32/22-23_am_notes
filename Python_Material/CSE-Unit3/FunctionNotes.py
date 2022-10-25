'''
     Abstraction - removes or simplifies the complexity
     Procedures - Purple Blocks
     Functions - Block of code that completes an algorithm
     Methods - Objects of classes can call specific algorithms
     
     Functions main purpose is to simplify and reuse code
     Two main types:
          to do - literally does a process
          return - returns a process' result
          ***EVERY function technically returns something - defaults to None***
     
     None Type -> an empty piece data, as in nothing is there, None data type
'''

#define the function
def howdy():
     #do this when I call the function
     print("howdy")
     
#call the function     
howdy()

# print("hello "+input('what is your name')+int(input('age')))

'''
     Functions we've used:
          input()
          print()
          int()    ord()   bin()   chr()
'''

#define a function that adds 2 numbers together
def adding():
     a=int(input("number 1 "))
     b=int(input("number 2 "))
     print(a+b)
     

#define a function to calc y when give mxb
def ymxb():
     m=int(input("m: "))
     x=int(input("x: "))
     b=int(input("b: "))
     print(m*x+b)
     
#pass in the variables
#set the arguments
def ymxb(m,x,b):
     print(m*x+b)     
     
#create x and y chart for first 10 numbers of y=1x+4
# for i in range(10):
#      # ymxb()
#      ymxb(1,i,4)

#define function x**2+4x+2         #x is a local variable
def parabola(x):
     # print(x**2+4*x+2)
     return x**2+4*x+2             #return gives back data to the program

print("x | y")
print("-----")
for i in range(6):
     print(f"{i} | {parabola(i)}")
     #HINT!!!  You may have an error!  Show Bander when you do!!!