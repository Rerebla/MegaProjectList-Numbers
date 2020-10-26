import math
binaryDecimal = input(
    "Type b for conversion to binary and d for conversion to decimal!")
number = int(input("Which Number would you want to convert?"))
if binaryDecimal == "b":
    binaryNumber = ""
    while number > 0:
        if number % 2 == 0:
            binaryNumber = "0" + binaryNumber
        else:
            binaryNumber = "1" + binaryNumber
        number = math.floor(number / 2)
    print(binaryNumber)
else:
    decimalNumber = 0
    counter = len(str(number)) - 1
    numberList = list(map(int, str(number)))
    for n in range(0, len(str(number))):
        decimalNumber = pow(numberList[counter] * 2, n) + decimalNumber
        counter -= 1
    if numberList[counter] == 0:
        decimalNumber -= 1
    print(decimalNumber)
