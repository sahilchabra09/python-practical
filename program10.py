#Name:- Sahil Chabra
# Btech ECE 1st sem
'''Write a program that returns the results of addition,
subtraction, multiplication, and division.'''

def add(a, b):
    print("Addition of two numbers:", a + b)

def sub(a, b):
    print("Subtraction of two numbers:", a - b)

def mul(a, b):
    print("Multiplication of two numbers:", a * b)

def div(a, b):
    if b == 0:
        print("Division by zero is not allowed.")
    else:
        print("Division of two numbers:", a / b)

x = int(input("Enter a number: "))
y = int(input("Enter a second number: "))

add(x, y)
sub(x, y)
mul(x, y)
div(x, y)
