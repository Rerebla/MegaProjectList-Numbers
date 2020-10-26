from math import pi
NthDigit = int(input("Up to wich digit would you want to know Pi?"))
if NthDigit <= 15:
    print(round(pi, NthDigit))
else:
    print("Too many digits! Limit: 15 (Due to float limitation)")
