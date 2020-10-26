import operator
firstRound = True
while True:
    inp = input(
        "Which operation would you want to make? Addision +, Subtration -, Multiplication *, Division /, to the Power of **? ")
    inp.replace(" ", "")
    if firstRound:
        numOne = int(input("Enter number 1. "))
    numTwo = int(input("Enter number 2. "))
    operatorDict = {
        "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv, "**": operator.pow
    }
    operation = operatorDict[inp]
    result = operation(numOne, numTwo)
    print(result)
    if input("Do you want to continue? yes/any  ") == "yes":
        numOne = result
        firstRound = False
    else:
        break
