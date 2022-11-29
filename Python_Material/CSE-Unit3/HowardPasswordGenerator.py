import random
password = []
#initializing questions
uppercase = int(input("enter preffered amount of uppercase letters: "))
lowercase = int(input("enter preferred amount of lowercase letters: "))
special = int(input("enter preferred amount of special: "))

#coding the for finding the numerical values for the password
for i in range (uppercase):
    upper = chr(random.randint(65,90))
    password.append(upper)
for i in range (lowercase):
    lower = chr(random.randint(97,122))
    password.append(lower)
for i in range (special):
    specialChar = chr(random.randint(33,44))
    password.append(specialChar)

#printing out the list for your password
print(password)
