# amountOwed = (float(input("change owed(in cents): ")))
# q=0
# d=0
# n=0
# p=0
# change = []
# # Quarters
# while (amountOwed) >= 0.25:
#     amountOwed = amountOwed - 0.25
#     q=q+1
#     amountOwed = round(amountOwed,2)
# change.append(f"quarters:{q}")

# # Dimes
# while (amountOwed) >= 0.10:
#     amountOwed = amountOwed - 0.10
#     d=d+1
#     amountOwed = round(amountOwed,2)
# change.append(f"Dimes:{d}")


# # nickels
# while (amountOwed) >= 0.05:
#     amountOwed = amountOwed - 0.05
#     n=n+1
#     amountOwed = round(amountOwed,2)
# change.append(f"nickels:{n}")

# # pennys
# while (amountOwed) >= 0.01:
#     amountOwed = amountOwed - 0.01
#     p=p+1
#     amountOwed = round(amountOwed,2)
# change.append(f"pennys:{p}")

# # check values
# print(amountOwed)
# print(change)

###############################
#did not see use modulo until I went to turn this in
###############################

amountOwed = (float(input("change owed(in cents): ")))
q=0
d=0
n=0
p=0
change = []
for quarters in range(float(amountOwed)):
    if quarters%0.25 ==  0:
        q=q+1
amountOwed=amountOwed-(q*0.25)
amountOwed = round(amountOwed,2)
print(f"quarters=",{q})
    
for dimes in range(amountOwed):
    if dimes%0.10==0:
        d=d+1
amountOwed=amountOwed-(d*0.10)
amountOwed = round(amountOwed,2)
print(f"dimes=",{d})
print(amountOwed)
