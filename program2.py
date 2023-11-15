#Name - Sahil Chabra
# Btech 1st sem
# To know if a number is zero, positive, or negative.
# Enter a number from the keyboard by the user.

num = int(input('Enter a number: '))

if num > 0:
    print(num, 'is positive')
elif num < 0:
    print(num, 'is negative')
else:
    print('Zero')
