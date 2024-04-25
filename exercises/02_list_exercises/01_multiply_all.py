# Write a Python script to multiply all the items in a list.
alist = [12, 43, 57, 98, 83, -103, 256, -1]
print(f'{alist=}')

# Solution 1 - Use for loop
product = 1
for i in alist:
    product *= i
print(f"The product is {product}.")

# Solution 2 - Use math module
import math
print(f"The product is {math.prod(alist)}.")

# Solution 3 - Use list comprehension
p = 1
print(f"The product is {[p:=p*i for i in alist][-1]}.")
