from math import e
NthDigit = int(input("Up to wich digit would you want to know E?"))
if NthDigit <= 15:
    print(round(e, NthDigit))
else:
    print("Too many digits! Limit: 15 (Due to float limitation)")
