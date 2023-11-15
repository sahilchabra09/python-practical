# Name: Sahil chabra
# Btech ECE 1st Sem
# Program to calculate factorial values using recursion.

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter a number: "))
print("Factorial of", n, "is", factorial(n))
