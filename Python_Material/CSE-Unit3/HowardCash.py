amountOwed = (float(input("change owed(in cents): ")))
q=0
d=0
n=0
p=0
change = []
# Quarters
while (amountOwed) >= 0.25:
    amountOwed = amountOwed - 0.25
    q=q+1
    amountOwed = round(amountOwed,2)
change.append(f"quarters:{q}")

# Dimes
while (amountOwed) >= 0.10:
    amountOwed = amountOwed - 0.10
    d=d+1
    amountOwed = round(amountOwed,2)
change.append(f"Dimes:{d}")


# nickels
while (amountOwed) >= 0.05:
    amountOwed = amountOwed - 0.05
    n=n+1
    amountOwed = round(amountOwed,2)
change.append(f"nickels:{n}")

# pennys
while (amountOwed) >= 0.01:
    amountOwed = amountOwed - 0.01
    p=p+1
    amountOwed = round(amountOwed,2)
change.append(f"pennys:{p}")

# check values
print(amountOwed)
print(change)