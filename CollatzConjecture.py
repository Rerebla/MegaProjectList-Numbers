output = 0
number = int(input(
    "Which number would you want to run through this algorithm? Has to be over 1."))
if number > 1:
    if number % 2 == 0:
        output = number.__truediv__(2)
    else:
        output = number.__mul__(3).__add__(1)
    print(output)
