def isprime(number):
    if n <= 1:
        return False
    for i in range(2, number):
        if (number % i == 0):
            return False
    else:
        return True


n = 0
while True:
    if input("Do you want to start/continue? y/n  ") == 'n':
        print("Stopped!")
        break
    while True:
        if isprime(n):
            print(n)
            n += 1
            break
        n += 1
