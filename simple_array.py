#!/usr/bin/env python3.6

"""
This module is an example of how arrays work in
python. Arrays in python are called 'list' and from
this point forward all array object, while be called list.
Written by: Esteban Fernandez and GPL3- License, as well as Swedish Copy Right Laws is enforced.

The module should solve the following assignments:

-   Create an list with 20 position
-   Exchange or fill the list-positions with letters
-   Sort the list in alphabetical order
-   Prompt to terminal the ordered list
-   Reverse the order of the ordered list i.e.
    A = 20 , B = 19 , C = 18 .. etc

Since, this is a script and not a module the if __name__ == "__main__" is skipped.
"""

# Importing standard modules
import string  # Get letters
import random as rnd  # Get randomization

# List comprehension picks letters randomly between (0) and (20)
list_of_letters = [rnd.choice(string.ascii_uppercase) for _ in range(0, 20)]

# Prompting Array of random sequence
print("Random sequence of letters:\n\n{0}\n\n Number of letters picked:\n {1}".format(
    list_of_letters, len(list_of_letters)))

# Ordering List in alphabetical order A-Z
list_of_letters.sort()

# Prompting ordered letters
print("\n\nOrdered letters:{}\n\n".format(list_of_letters))

# Reversing Order of List from A-Z to Z-A
list_of_letters.reverse()  # It's also possible to do list[::-1]

# Prompting list
print("\n\nReversed Order:{}\n\n".format(list_of_letters))

# Copying list
old_list_with_letters = list_of_letters.copy()  # This a shallow copy not a true copy

# Representing letters in list_of_letters as Unicode Point Numbers
list_of_digits = list(map(ord, list_of_letters))  # map(function, iterable) --> Unicode numbers

# Creating Generator with tuple(Letter, Converted to Digit)
letters_to_digits = zip(old_list_with_letters, list_of_digits)

# Prompting Results
print("\n\nLetters converted to UniCode points {}\n\n".format(tuple(letters_to_digits)))

print("\n\nThe converted list: {}\n\n".format(list_of_digits))




