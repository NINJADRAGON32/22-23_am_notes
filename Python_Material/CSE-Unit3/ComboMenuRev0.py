# PLTW 3.1.3
# Simulate someone ordering at a fast food resturaunt
#global variables defined in first couople lines
total=0
orderInformation=""

#sandwich
#ask the user if they would like a chicken beef or tofu 
sandwich = input("Which sandwich would you like: chicken $5.25, beef $6.25, tofu $5.75 (c,b,t)")
if sandwich=="c":
    total+=5.25
elif sandwich=="b":
    total+=6.25
elif sandwich=="c":
    total+=5.75
orderInformation+=f"sandwich:\t{sandwich}\n"
#\t = tab
#\n = new line

#drinks
drink = input("would yopu like a drink? (y/n)")
if drink =="y":
    drink = input("which size would you like? s,m,l")
    if drink == "s":
        total+=1
    elif drink == "m":
        total+=1.75
    elif drink == "l":
        drink = input("Would you like a child size for $.38 more (y,n)")
        if drink == "y":
            total+=(2.25+.38)
            drink = "c"
        else:
            total+=2.25
            drink="1"
orderInformation+=f"drink:\t{drink}\n"
#fries
fries = input("would you like fries (y/n)")
if fries =="y":
    fries = input(" what size would you like (s,m,l)")
    if fries== "m":
        total+= 1.50
    elif fries == "l":
        total+=2.00
    elif fries == "s":
        fries = input ("would you like to supersize your fries (y/n)")
        if fries== "y":
            total+=2.00
            fries="l"
        else:
            fries == "s"
            total += 1
orderInformation+=f"fries:\t{fries}\n"
#ketchup



#checkout
print(orderInformation)
print(total)
# hint hint wink wink look up how to round later
#discount
if sandwich !="n" and drink!="n" and fries!="n":
    total-=1
    print("discount applied")
else:
    print("discount not applicable")