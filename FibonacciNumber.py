NthNumber = int(
    input("For which number would you want to have the FibonacciNumber?"))
x = 0
y = 1
oldY = 0
for i in range(NthNumber - 1):
    oldY = y
    y += x
    x = oldY
print(y)
