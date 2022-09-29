print(int("15"))  #change "15" to an int
print(str("15"))      #chnge"15" to a string 
print(bool("15"))    #change "15" to true"
print(bool("-15"))     #change "15" to true 

#for a boolean data type any other number besides 0 is true
#in java: String

print(float("15"))       #change "15" to a float
print(type("15"))         #tells the data type
print(232/5)

print("-----------------------------------------------------")
print(int(3.14159))
print(int("8675309"))
print(bool(0))
print(bool(1))
print(float(10))

# conditional statments -> if statement -> if elif else

x=int(input("give me a number"))
if(x<10):
    print("too low")
elif(x>10):
    print("toohigh")
else:
    print("you got it!!!")

# you can use a space of your a monster must utilize tabs

# if (boolean):
#   then portion
# nested -> a bird is stitting in the nest -> indented inside of the nest 

food = input("did you eat breakfast")
if (food=="yes"):
    what = input("what did you eat for bfast")
    if (what=="waffles"):
        t= input("what type of waffles")
        if (t=="chocolate chip"):
            print("bluebery is superior")
