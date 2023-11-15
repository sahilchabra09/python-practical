# Name: Sahil Chabra
# Btech ECE 1st sem
# Program to display stars in an equilateral triangular form.

n = 12  # You can adjust the value of n to control the size of the triangle.

for i in range(1, n + 1):
    print(" " * (n - i), end="")  # Print leading spaces
    print("*" * (2 * i - 1))      # Print stars
