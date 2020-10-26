import math
# region Money
twenty = 20.0
ten = 10.0
five = 5.0
dollar = 1.0
quarter = 0.25
dime = 0.1
nickel = 0.05
penny = 0.01
moneyValues = [twenty, ten, five, dollar, quarter, dime, nickel, penny]
# endregion
ammount = float(input("How much does the purchase cost?"))
moneyGiven = float(input("How much did the customer pay?"))
difference = round(moneyGiven - ammount, 2)
if difference <= 0:
    print("Customer didn't pay enough")

for value in moneyValues:
    while difference - value >= 0:
        print(value)
        difference = round(difference - value, 2)
