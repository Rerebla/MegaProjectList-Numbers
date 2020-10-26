creditCardNumber = str(input("What is the credit card number? "))
sumOfDigits = 0
for x in range(0, len(creditCardNumber)):
    if x % 2 == 0:
        sumOfDigits += int(sum(list(map(int,
                                        str(int(creditCardNumber[x]) * 2)))))
    else:
        sumOfDigits += int(creditCardNumber[x])
if sumOfDigits % 10 == 0:
    print("Valid!")
else:
    print("Invalid")
