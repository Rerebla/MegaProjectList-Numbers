unitOne = ""
unitTwo = ""
ouput = 0
category = input(
    "In which unit category would you want to convert something? [1]temperature [2]volume [3]currency [4]mass  ")
numberOne = int(input("What number would you want to convert?"))
if category == "1":
    unitOne = input("What is your first unit? F/C/K  ")
    unitTwo = input("What is your second unit? F/C/K  ")

    def FahrenheitToCelsius(num):
        return (numberOne - 32) * 5 / 9

    def FahrenheitToKelvin(num):
        return KelvinToCelsius(FahrenheitToCelsius(num))

    def CelsiusToFahrenheit(num):
        return (num * 9 / 5) + 32

    def CelsiusToKelvin(num):
        return num - 273.15

    def KelvinToCelsius(num):
        return num + 273.15

    def KelvinToFahrenheit(num):
        return CelsiusToFahrenheit(KelvinToCelsius(num))

    if unitOne == "F" and unitTwo == "C":
        print(FahrenheitToCelsius(numberOne))
    elif unitOne == "F" and unitTwo == "K":
        print(FahrenheitToKelvin(numberOne))
    elif unitOne == "C" and unitTwo == "F":
        print(CelsiusToFahrenheit(numberOne))
    elif unitOne == "C" and unitTwo == "K":
        print(CelsiusToKelvin(numberOne))
    elif unitOne == "K" and unitTwo == "C":
        print(KelvinToCelsius(numberOne))
    elif unitOne == "K" and unitTwo == "F":
        print(KelvinToFahrenheit(numberOne))
    else:
        print("Something was wrong about the unit input")
