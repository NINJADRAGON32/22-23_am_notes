file1 = open("StudentDatabase.txt","r")
f = file1.readlines()


for line in f:
    #print the line and strip everything to the right
    print(line.rstrip())