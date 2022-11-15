file1 = open("StudentDatabase.txt","r")
f = file1.readlines()


for line in f:
    #print the line and strip everything to the right
    print(line.rstrip())
    

### WRITE TO A FILE
# wat file are we writing to
fileToWriteTo = open("The New File.txt","w")
fileToWriteTo.write("Hello World, how U?")
fileToWriteTo.close()