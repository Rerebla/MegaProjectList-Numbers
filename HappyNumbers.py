#  Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1
num = input("Number: ")
numList = []


def sumOfSquareOfDigits(number):
    number = str(number)
    result = 0
    for x in number:
        x = int(x)
        result += pow(x, 2)
    return result


while True:
