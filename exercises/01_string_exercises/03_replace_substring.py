# Write a Python script to ask for a string and two substrings,
# and print the string with all occurrences of the first substring
# replaced by the second substring.
# E.g.
# Enter a string: Hello world!
# Enter substring to replace: world
# Enter replacement substring: Python
# Hello Python!
s = input("Enter a string: ")
ss1 = input("Enter substring to replace: ")
ss2 = input("Enter replacement substring: ")
print(s.replace(ss1, ss2))
