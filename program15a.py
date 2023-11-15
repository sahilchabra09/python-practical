#Name:- Sahil Chabra
# Btech ECE 1st sem
'''Program to access each element of a string in forward
and reverse order using for and while loop.'''

# Input a string
input_string = input("Enter a string: ")

# Using a for loop to access elements in forward order
print("Accessing elements in forward order using a for loop:")
for char in input_string:
    print(char, end=' ')
print()  # Print a newline for formatting

# Using a while loop to access elements in reverse order
print("Accessing elements in reverse order using a while loop:")
length = len(input_string)
index = length - 1

while index >= 0:
    print(input_string[index],end=' ')
    index -= 1

# Print a newline for formatting
print()

