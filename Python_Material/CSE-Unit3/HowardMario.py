height = 0
height = int(input("desired height= "))
#r=row
#c=column

for r in range(1, height + 1):
    for c in range(1, height+1):
        if c > (height - r):
            print("#", end="")
        else:
            print(" ",end=" ")
        
        if c==height:
            print(" ","#" *r, end= "")
    print()



