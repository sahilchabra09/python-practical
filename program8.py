#Name:- Sahil Chabra
# Btech ECE 1st sem
# Write a program to calculate factorial values of numbers using functions.

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

n = int(input("Enter your number: "))
factorial_value = factorial(n)
print("The factorial of", n, "is", factorial_value)
