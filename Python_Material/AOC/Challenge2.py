with open("day2.txt","r") as f:
    file = f.readlines()
    
    
print(file)

newFile=[]
for line in file:
    opp,me=line.rstrip().replace(" ","")
    newFile.append(f"{opp}{me}")
print(newFile)

combos={"AX":3,
        "AY":4,
        "AZ":8,
        "BX":1,
        "BY":5,
        "BZ":9,
        "CX":2,
        "CY":6,
        "CZ":7
    }

total=0
for line in newFile:
    total+=combos[line]
    
print(total)