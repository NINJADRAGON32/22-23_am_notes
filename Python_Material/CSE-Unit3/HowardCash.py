amountOwed = (float(input("change owed(in cents): ")))
q=0
d=0
n=0
p=0
change = []
# def coinsOwed(amountOwed):
while (amountOwed) >= 0.25:
    amountOwed = amountOwed - 0.25
    q=q+1
change.append(f"quarters:{q}")
print(change)
print(amountOwed)
while (amountOwed) >= 0.10:
    amountOwed = amountOwed - 0.10
    d=d+1
change.append(f"Dimes:{d}")
    
print(change)
print(amountOwed)