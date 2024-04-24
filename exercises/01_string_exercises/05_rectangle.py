# Write a Python script to ask for the length and width of a rectangle, 
# calculate and print the perimeter and area of the rectangle.
# E.g.
# Enter length: 1.5
# Enter width: 4
# perimeter = 11.0, area = 6.0

l = float(input("Enter length: "))
w = float(input("Enter width: "))

perimeter = 2*l + 2*w
area = l * w
print(f"{perimeter = }, {area = }")
