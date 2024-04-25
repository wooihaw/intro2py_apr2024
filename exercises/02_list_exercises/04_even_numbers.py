# Write a Python script that takes a list of numbers and returns a new list containing only the even numbers from the original list.
alist = [12, 43, 57, 98, 83, -103, 256, -55, 168, -6]
print(f'{alist=}')

# Use for loop
even1 = []
for n in alist:
    if n % 2 == 0:
        even1.append(n)
print(f"{even1 = }")

# Use list comprehension
even2 = [n for n in alist if n % 2 == 0]
print(f"{even2 = }")