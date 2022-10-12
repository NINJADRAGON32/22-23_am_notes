import random
#print out randam characters onto the screen
# hint hint wink wink 0-9a-z!@(*&#^%$%#$@!@#$%)
#may want this for later

#generate a random character - asci table
#print (chr(97))

#create a string of characters

while(True):
    out=""
    #concatenate 10 characters
    i=0
    while(i<=430000000):
        out+=chr(random.randint(32,126))
        i+=1
    print(out)
