# CY83R-3X71NC710N
import random

print("Welcome to the shape maker!")

choices = ["Square","Rectangle","Lower Left Triangle","Upper Left Triangle","Diamond"]
print("Choose a type of shape from the following list: ")
print(choices)
shape = input("> ")

while shape not in choices:
	print("Invalid choice please enter correctly")
	shape = input("> ")

while not isinstance(shape, str):
    print("Incorrect input please fix")
    shape = input("> ")

if shape == "Square":
    # Draw a square. This shape is done for you.
    print("Side length:")
    x = input("> ")
    x = int(x)
    for row in range(x):
        for col in range(x):
            print("@",end="")
        print()

elif shape == "Rectangle":
    print("Side length:")
    x = input("> ")
    x = int(x)
    for row in range(random.randint(1,10)):
        for col in range(x):
            print("@",end="")
        print()
    pass

elif shape == "Lower Left Triangle":
    print("Side length:")
    x = input("> ")
    x = int(x)
    for row in range(x):
        for col in range(row): # Runs 1x for the first row, 2x for the second row, etc.
            print("@",end="")
        print()

elif shape == "Upper Left Triangle":
    print("Side length:")
    x = input("> ")
    x = int(x)
    for row in range(x):
        for col in range(x - 1, row - 1, -1):
            print("@", end="")
        print()
    
elif shape == "Diamond":
    print("Radius:")
    x = input("> ")
    x = int(x)
    print("Creating Diamond")

    for row in range(x):
        spaces = " " * (x - row - 1)
        stars = "#" * (2 * row + 1)
        print(spaces + stars)

    for row in range(x - 2, -1, -1):
        spaces = " " * (x - row - 1)
        stars = "#" * (2 * row + 1)
        print(spaces + stars)
