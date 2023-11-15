# Name: Sahil Chabra
# Btech ECE 1st sem
# Program to generate a Fibonacci series.

n = int(input("How many Fibonacci numbers do you want?"))

# First two Fibonacci numbers
f1 = 0
f2 = 1

# Counter to keep track of the number of Fibonacci numbers generated
count = 2

if n == 1:
    print(f1)
elif n == 2:
    print(f1, '\n', f2, sep='')
else:
    print(f1, '\n', f2, sep='')

    while count < n:
        fib = f1 + f2
        print(fib)
        f1 = f2
        f2 = fib
        count += 1

print()  # To add a newline at the end for formatting
