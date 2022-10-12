#loops-> to repeat your code as many times as needed


# while loops
# while (something is true): -> while(boolean expression):
#       do something

# for loop

# print out the numbers 0-9
i=0     #iterator-> variable to help with iteration
while(i<=9):
    print(i)    #do something
    i+=1    #iterates the loop

# infinite loop -> loop that never ends

#print out 0-9 only even
while(i<=9):
    print(i)    
    i+=2

#check for ui
ui=input("guess what")
correctAnswer=["what","What","WAT","wat","wut","WUT","WAOT","waot","WHAT","Wut","Waaaa","Que","Yeah","Huh","Nani"]
while(not(ui in correctAnswer)):
    ui=input("guess what")
print("chicken butt")

# while(ui != correctAnswer)
# while(str != list)
# for loops 