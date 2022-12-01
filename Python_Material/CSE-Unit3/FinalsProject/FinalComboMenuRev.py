subtotal=0
total=0
orderInformation=""
order=[]
totalOrder=("")


#procedures for Order Loop

'''
    To order, state whether you would like a; Krabby Patty(kp), Coral Bits(cb) ,Kelp Rings (Kr) , 
    Footlong (fl) , Krabby Meal (km) , 
'''


def sandwichFunc():
    global subtotal
    invalidInput=(0)
    while invalidInput==(0):
        sandwich = input("Which sandwich would you like: Krabby Patty  $1.25, Double Krabby Patty  $2.00, Tripple Krabby Patty $3.00 (s,d,t): ")
        if sandwich=="s":
            cheese = input("would you like chees with that?(y/n)")
            if cheese == "n":
                subtotal+=1.25
                order.append("Krabby Patty")
                #iterator
                invalidInput=(invalidInput+1)
            elif cheese == "y":
                subtotal+=1.50
                order.append("Krabby Patty w/ Cheese")
                invalidInput=(invalidInput+1)
        elif sandwich=="b":
            cheese = input("would you like chees with that?(y/n)")
            if cheese == "n":
                subtotal+=2.00
                order.append("Double Krabby Patty")
                #iterator
                invalidInput=(invalidInput+1)
            elif cheese == "y":
                subtotal+=2.25
                order.append("Double Krabby Patty w/ Cheese")
                invalidInput=(invalidInput+1)
        elif sandwich=="t":
           cheese = input("would you like chees with that?(y/n)")
        if cheese == "n":
                subtotal+=3.00
                order.append("Triple Krabby Patty")
                #iterator
                invalidInput=(invalidInput+1)
        elif cheese == "y":
                subtotal+=3.25
                order.append("Triple Krabby Patty w/ Cheese")
                invalidInput=(invalidInput+1)
        else: 
            print("try again, Invalid Input")

def sandwichMealFunc():
    global subtotal
    invalidInput=(0)
    while invalidInput==(0):
        sandwich = input("Which meal would you like: single $3.50, Double $3.75, Tripple $4.00 (k,d,t): (s,d,t) ")
        if sandwich=="s":
            subtotal+=3.50
            order.append("Krabby Patty")
            #iterator
            invalidInput=(invalidInput+1)
        elif sandwich=="b":
            subtotal+=3.75
            order.append("Double Krabby Patty")
            #iterator
            invalidInput=(invalidInput+1)
        elif sandwich=="t":
                subtotal+=4.00
                order.append("Triple Krabby Patty")
                #iterator
                invalidInput=(invalidInput+1)
        else: 
            print("try again, Invalid Input")

def drinkFunc():
    global subtotal
    invalidInput=(0)
    while invalidInput==(0):
        type = input("would you like a seafoam soda(ss) or a kelp shake(ks)?")
        if type =="ss":
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
                subtotal+=2.25
                order.append("Large drink")
                drink="l"
                invalidInput=(invalidInput+1)
            else: 
                print("try again, Invalid Input")
        elif type == "ks":
            subtotal+=2.00
            order.append("kelp Shake")
            invalidInput=(invalidInput+1)
            drink = "ks"

def friesFunc():
    global subtotal
    invalidInput=(0)
    while invalidInput==(0):
        fries = input(" what size would you like (s,m,l): ")
        if fries== "m":
            subtotal+= 1.25
            order.append("Medium CB")
            invalidInput=(invalidInput+1)
        elif fries == "l":
            subtotal+=1.50
            order.append("Large CB")
            invalidInput=(invalidInput+1)
        elif fries == "s":
            subtotal += 1
            order.append("Small CB")
            invalidInput=(invalidInput+1)
        else:
            print("try again, Invalid Input")

def footlong():
    global subtotal
    invalidInput=(0)
    while invalidInput==(0):
        confirm = input("the foot long is $2.00 would you like to add it to your final order (y,n)")
        if confirm == "y":
        
        
    
# def kpacketFunc():
#     global subtotal
#     price_of_kPacket=0
#     invalidInput=(0)
#     while invalidInput==(0):
#         kPacket = input ("how many would you like?: ")
#         kPacket = int(kPacket)
#         if kPacket >= 0:
#             order.append(f"{kPacket} Ketchup packets")
#             price_of_kPacket=kPacket*0.25
#             subtotal += price_of_kPacket
#             invalidInput=(invalidInput+1)
        

#while loop to continue ordering
# Order=input("Hi welcome to Galley Grub May I take Your order(y/n) ")
# if Order=="y":
#     while totalOrder!="y":
#         #procedure for getting the sandwich order is on line 84
#         sandwich=input(" would you like another sandwich(y/n): ")
#         if sandwich==("y"):
#             sandwichFunc()
        
#         #procedure for getting the drink order is on line 97
#         drink = input("would you like a drink? (y/n): ")
#         if drink =="y":
#             drinkFunc()

#         #procedure for ordering fries is on line 117
#         fries=input("would you like some fries(y/n): ")
#         if fries=="y":
#             friesFunc()

#         #procedure for ketchup packets is on line 137
#         kPacket=input("would you like some more Ketchup packets?(y/n): ")
#         if kPacket=="y":
#             kpacketFunc()
        
#         totalOrder=input("will that be all for you today?(y/n): ")
            





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