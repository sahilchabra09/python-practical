#Name:- Sahil Chabra
# Btech ECE 1st sem
''' To write a program to accept numeric digit
from keyboard and display it in words.'''

a = int(input("Enter a numeric digit: "))

if a == 0:
    print("zero")
elif a == 1:
    print("one")
elif a == 2:
    print("two")
elif a == 3:
    print("three")
elif a == 4:
    print("four")
elif a == 5:
    print("five")
elif a == 6:
    print("six")
elif a == 7:
    print("seven")
elif a == 8:
    print("eight")
elif a == 9:
    print("nine")
else:
    print("Invalid input. Please enter a numeric digit between 0 and 9.")
