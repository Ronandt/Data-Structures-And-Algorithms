# Refer to Python’s documentation on its array module:
# • https://docs.python.org/3/library/array.html
#
#
# Write a Python program that performs the following:
# a) Create an array of integers, array_int
# b) Initialise array_int with the following values [1, 5, 7, 9, 100]
# c) Insert the number 3 into the second element of array_int
# d) Remove the number 100 from array_int
# e) Append the number 11 into array_int
# f) Reverse the order of the numbers in array_int
# [NOTE: Print out the content of array_int after every step to verify correctness of your code.]

import array as arr

array_int = arr.array('i', [1, 5, 7, 9, 100])
print(array_int)

array_int.insert(1, 3)
print(array_int)

array_int.pop(-1)
print(array_int)

array_int.append(11)
print(array_int)

array_int.reverse()
print(array_int)
