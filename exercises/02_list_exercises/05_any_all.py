# Write a Python script to check if any of the numbers in the list is greater than 100.
# If so, print True. Otherwise, print False.
# Furthermore, print True if all the numbers in the list are greater than 50. Otherwise, print False.
alist = [74, 88, 90, 73, 74, 61, 74, 90, 56, 56, 100, 59, 85, 54, 99]
print(f'{alist=}')

# Use any() to check if any number is greater than 100
print(any([True if n > 100 else False for n in alist]))

# Use all() to check if all numbers are greater than 50
print(all([True if n > 50 else False for n in alist]))