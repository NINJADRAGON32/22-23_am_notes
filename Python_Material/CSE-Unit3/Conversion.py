#in to cm
def in2cm():
     inches = int(input("inches: "))
     print(inches*2.54)
def cm2in():
     cm = int(input("cm: "))
     print(cm/2.54)
     
#kg to grams - owen
def kg2g():
     kg = int(input("kilograms: "))
     print(kg*1000)
def g2kg():
     g = int(input("grams: "))
     print(g/1000)

#milli to inches - parker
def mi2in():
     inches=int(input("inches: "))
     print(inches*1000)
def in2mi():
     mi=int(input("milli: "))
     print(mi/0.393701)

#meters to feet - dieekman
def m2ft():
     m = int(input("m:  "))
     print(m*3.28)
def ft2m():
     ft = int(input("ft:  "))
     print(ft/3.28)

#centimeter to meters - jonah
def cm2m():
     cm = int(input("cm: "))
     print(cm/100)
def m2cm():
     m = int(input("m: "))
     print(m*100)

#milli to centi - stevenen
def milli2cm():
    milli = int(input("millimeters: "))
    print(milli*10)
def cm2milli():
    cm = int(input("cm: "))
    print(cm/10)

#ounces to cup - gillet
def oz2cup():
     ounces = int(input("ounces:"))
     print(ounces*0.125)
def cup2oz():
     cup = int(input("cup: "))
     print(cups/0.125)

#teaspoon to Tablespoon - Steckler
def tbsp2tsp():
     tbsp=int(input("Tablespoons: "))
     print(tbsp*3)
def tsp2Tbsp():
     tsp = int(input("Teaspoons: "))
     print(tsp/3)

#Joules to Watts - gad
def j2w():
     joules = int(input("Joules per second: "))
     print (joules*1+"Watts")
def w2j():
     watts = int(input("watts: "))
     print(watts * 1)

#m/s to ft/s - charity
def m2ft():
     meters = int(input("meters:"))
     print(meters*3.28)
def ft2m():
    feet =int(input("feet:"))
    print(feet/3.28)

#atoms in a molecule - landon
def moles2atoms():
     moles=float(input("moles"))
     print(moles*(6.02*10**23))	
def atoms2moles():
	atoms=float(input("atoms"))
	print(atoms/(6.02*10**23))

#you can keep adding
