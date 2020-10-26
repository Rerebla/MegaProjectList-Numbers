from math import sqrt
number = int(input("Which number would you like to have Primefactorized?"))
while number % 2 == 0:
    number = number/2
    print(2)
for i in range(3, int(sqrt(number)) + 1):
    while (number % i == 0):
        print(i)
        number = number/i
if number > 2:
    print(int(number))
