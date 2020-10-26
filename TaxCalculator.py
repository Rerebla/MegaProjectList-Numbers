import math
tax = int(input("Enter your tax: "))
purchaseCost = float(input("Enter your purchase cost:  "))
total = 0
tax = (tax / 100) + 1
total = purchaseCost * tax
print(round(total, 2))
