subtotal=0
total=0
orderInformation=""
order=[]
totalOrder=("")


#procedures for Order Loop

def sandwichFunc():
    global subtotal
    invalidInput=(0)
    while invalidInput==(0):
        sandwich = input("Which sandwich would you like: chicken $5.25, beef $6.25, tofu $5.75 (c,b,t): ")
        if sandwich=="c":
            subtotal+=5.25
            order.append("Chimken sandwich")
            #iterator
            invalidInput=(invalidInput+1)
        elif sandwich=="b":
            subtotal+=6.25
            order.append("Beef sandwich")
            invalidInput=(invalidInput+1)
        elif sandwich=="t":
            order.append("Tofu sandwich")
            subtotal+=5.75
            invalidInput=(invalidInput+1)
        else: 
            print("try again, Invalid Input")

def drinkFunc():
    global subtotal
    invalidInput=(0)
    while invalidInput==(0):
        drink = input("which size would you like? s,m,l: ")
        if drink == "s":
            subtotal+=1
            order.append("small drink")
            invalidInput=(invalidInput+1)
        elif drink == "m":
            subtotal+=1.75
            order.append("medium drink")
            invalidInput=(invalidInput+1)
        elif drink == "l":
            drink = input("Would you like a child size for $.38 more (y,n): ")
            if drink == "y":
                subtotal+=(2.25+.38)
                order.append("Child sized drink")
                drink = "c"
                invalidInput=(invalidInput+1)
            else:
                subtotal+=2.25
                order.append("Large drink")
                drink="l"
                invalidInput=(invalidInput+1)
        else: 
            print("try again, Invalid Input")

def friesFunc():
    global subtotal
    invalidInput=(0)
    while invalidInput==(0):
        fries = input(" what size would you like (s,m,l): ")
        if fries== "m":
            subtotal+= 1.50
            order.append("Medium Fry")
            invalidInput=(invalidInput+1)
        elif fries == "l":
            subtotal+=2.00
            order.append("Large Fry")
            invalidInput=(invalidInput+1)
        elif fries == "s":
            fries = input ("would you like to supersize your fries (y/n): ")
            if fries== "y":
                subtotal+=2.00
                order.append("Large Fry")
                fries="l"
                invalidInput=(invalidInput+1)
            else:
                fries == "s"
                subtotal += 1
                order.append("Small Fry")
                invalidInput=(invalidInput+1)
        else:
            print("try again, Invalid Input")

def kpacketFunc():
    global subtotal
    price_of_kPacket=0
    invalidInput=(0)
    while invalidInput==(0):
        kPacket = input ("how many would you like?: ")
        kPacket = int(kPacket)
        if kPacket >= 0:
            order.append(f"{kPacket} Ketchup packets")
            price_of_kPacket=kPacket*0.25
            subtotal += price_of_kPacket
            invalidInput=(invalidInput+1)
        

#while loop to continue ordering
Order=input("Hi welcome to McDonalds May I take Your order(y/n) ")
if Order=="y":
    while totalOrder!="y":
        #procedure for getting the sandwich order is on line 84
        sandwich=input(" would you like another sandwich(y/n): ")
        if sandwich==("y"):
            sandwichFunc()
        
        #procedure for getting the drink order is on line 97
        drink = input("would you like a drink? (y/n): ")
        if drink =="y":
            drinkFunc()

        #procedure for ordering fries is on line 117
        fries=input("would you like some fries(y/n): ")
        if fries=="y":
            friesFunc()

        #procedure for ketchup packets is on line 137
        kPacket=input("would you like some more Ketchup packets?(y/n): ")
        if kPacket=="y":
            kpacketFunc()
        
        totalOrder=input("will that be all for you today?(y/n): ")
            





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












