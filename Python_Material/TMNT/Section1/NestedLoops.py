


# low = 0
# high = 10
# for i in range (10):
#     for i in range(low,high):
#         print(i,end=" ")
#     print()
#     low = low+10
#     high = high +10
    
for row in range (10):
    for col in range(10):
        print(f"{col}{row}",end="")
    print()