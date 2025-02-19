# 1. Given a side of square. Find its perimeter and area.

side = int(input("Input the value for the side of square: "))
perimeter = side * 4
area = side ** 2

print("Perimeter: ", perimeter)
print("Area: ", area, "\n\n")

# 2. Given diameter of circle. Find its length.

diameter = int(input("Input the diameter of a circle: "))
radius = diameter / 2
p = 3.14
length = 2 * p * radius

print("Length of the circle: ",  length, "\n\n")

# 3. Given two numbers a and b. Find their mean.

a = int(input("Input the value of a: "))
b = int(input("Input the value of b: "))
mean = (a + b) / 2
print("Mean value of a and b: ", mean, "\n\n")

# 4. Given two numbers a and b. Find their sum, product and square of each number.

a = int(input("Input the value of a: "))
b = int(input("Input the value of b: "))
sum = a + b
product = a * b
square_a = a**2
square_b = b**2

print("Sum: ", sum, "\nProduct: ", product, "\nSquare of a: ", square_a, "\nSquare of b: ", square_b)