#Name:- Sahil Chabra
# Btech ECE 1st sem 
# Program to enter even numbers between m and n.

m = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))

if m % 2 != 0:
    m += 1

for i in range(m, n + 1, 2):
    print(i)
