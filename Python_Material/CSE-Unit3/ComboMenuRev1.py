subtotal=0
total=0
orderInformation=""
order=[]

#sandwich

#ask the user if they would like a chicken beef or tofu 
likeSandwich=input(" would you like a sandwich(y/n): ")
if likeSandwich==("y"):
    sandwich = input("Which sandwich would you like: chicken $5.25, beef $6.25, tofu $5.75 (c,b,t): ")
    if sandwich=="c":
        subtotal+=5.25
        order.appen("Chimken sandwich")
    elif sandwich=="b":
        subtotal+=6.25
        order.append("Beef sandwich")
    elif sandwich=="t":
        order.append("Tofu sandwich")
        subtotal+=5.75
    
orderInformation+=f"sandwich:\t{sandwich}\n"
#\t = tab
#\n = new line

#drinks
drink = input("would you like a drink? (y/n): ")
if drink =="y":
    drink = input("which size would you like? s,m,l: ")
    if drink == "s":
        subtotal+=1
        order.append("small drink")
    elif drink == "m":
        subtotal+=1.75
        order.append("medium drink")
    elif drink == "l":
        drink = input("Would you like a child size for $.38 more (y,n): ")
        if drink == "y":
            subtotal+=(2.25+.38)
            order.append("Child sized drink")
            drink = "c"
        else:
            subtotal+=2.25
            order.append("Large drink")
            drink="l"
orderInformation+=f"drink:\t{drink}\n"

#fries
fries = input("would you like fries (y/n): ")
if fries =="y":
    fries = input(" what size would you like (s,m,l): ")
    if fries== "m":
        subtotal+= 1.50
        order.append("Medium Fry")
    elif fries == "l":
        subtotal+=2.00
        order.append("Large Fry")
    elif fries == "s":
        fries = input ("would you like to supersize your fries (y/n): ")
        if fries== "y":
            subtotal+=2.00
            order.append("Large Fry")
            fries="l"
        else:
            fries == "s"
            subtotal += 1
            order.append("Small Fry")
orderInformation+=f"fries:\t{fries}\n"

#ketchup
price_of_kPacket=0
kPacket = input("would you like any ketchup packets? (y/n): ")
if kPacket =="y":
    kPacket = input ("how many would you like?: ")
    kPacket = int(kPacket)
    if kPacket  >= 0:
        order.append(f"{kPacket} Ketchup packets")
        price_of_kPacket=kPacket*0.25
        subtotal += price_of_kPacket
orderInformation+=f"ketchup packets:\t{kPacket}\n"

# totalOrder=input("Hi welcome to McDonalds May I take Your order(y/n) ")
# while totalOrder!="y":






#checkout
# hint hint wink wink look up how to round later
#discount
if sandwich !="n" and drink!="n" and fries!="n":
    subtotal-=1
    print("discount applied")
else:
    print("discount not applicable")

total=subtotal*1.07+total
    #https://www.tutorialspoint.com/How-to-round-down-to-2-decimals-a-float-using-Python
    #rounding
total=round(total,2)
print(orderInformation)
print(f"subtotal: {subtotal}")
print(f"total: {total}")
print(order)








#procedures for Order Loop
def sandwich():
    global subtotal
    sandwich = input("Which sandwich would you like: chicken $5.25, beef $6.25, tofu $5.75 (c,b,t): ")
    if sandwich=="c":
        subtotal+=5.25
        order.appen("Chimken sandwich")
    elif sandwich=="b":
        subtotal+=6.25
        order.append("Beef sandwich")
    elif sandwich=="t":
        order.append("Tofu sandwich")
        subtotal+=5.75

def Drink():
    global subtotal
    drink = input("which size would you like? s,m,l: ")
    if drink == "s":
        subtotal+=1
        order.append("small drink")
    elif drink == "m":
        subtotal+=1.75
        order.append("medium drink")
    elif drink == "l":
        drink = input("Would you like a child size for $.38 more (y,n): ")
        if drink == "y":
            subtotal+=(2.25+.38)
            order.append("Child sized drink")
            drink = "c"
        else:
            subtotal+=2.25
            order.append("Large drink")
            drink="l"