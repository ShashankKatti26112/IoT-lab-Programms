import math

shape = input("Enter the shape (circle, triangle, rectangle): ").lower()

if shape == "circle":
    radius = float(input("Enter the radius: "))
    area = math.pi * radius**2
elif shape == "triangle":
    base = float(input("Enter the base length: "))
    height = float(input("Enter the height: "))
    area = 0.5 * base * height
elif shape == "rectangle":
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area = length * width
else:
    print("Invalid shape entered.")
    area = None

if area is not None:
    print(f"Area of the {shape}: {area}")
