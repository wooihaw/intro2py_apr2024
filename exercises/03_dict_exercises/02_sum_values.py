# Write a Python script to print the sum of all values in the dictionary where the values are numbers.
# Expected results:
# adict =  {'a': 66, 'b': 33, 'c': 39, 'd': 7, 'e': 80, 'f': 5, 'g': 9}
# Sum of all values in the dictionary: 239

adict =  {'a': 66, 'b': 33, 'c': 39, 'd': 7, 'e': 80, 'f': 5, 'g': 9}

# Method 1 - Use for loop
total = 0
for k in adict:
    total += adict[k]
print(f"Sum of all values: {total}")

# Method 2 - Use dictionary comprehension with sum()
print(f"Sum of all values: {sum({adict[k]:k for k in adict})}")

# Method 3 - Use dictionary values() method with sum()
print(f"Sum of all values: {sum(adict.values())}")
