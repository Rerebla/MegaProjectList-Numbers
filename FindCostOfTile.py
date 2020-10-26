print("All measurements are done in the metric system and with euros!")
cost = int(input(
    "Assuming you are buying by the square meter. How much does a single square meter of tiling cost? "))
if input("Do you know the dimensions of your room in square meters? yes/any ") == "yes":
    overallDimensions = int(input("How big is your room?"))
    print("Cost:")
    print(cost * overallDimensions)

else:
    print("Assuming your room is quadratic.")
    heigth = int(input("Which height does the floor have? "))
    width = int(input("Which width does the floor have? "))
    print("Cost:")
    print(heigth * width * cost)
