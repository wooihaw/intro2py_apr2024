# This file contains the samples codes for "List and Tuple" section.

# %% List (1)
# Combination of strings, numbers and a list
mixed_list = [7, 'abc', 3.142, [1.5, 2]]
mixed_list[2] = 3.142
# Empty list
empty_list = []

# %% List (2)
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
some_nums = nums[2:7]
print(nums[0])  # first item
print(nums[-1]) # last item

# %% List (3)
alist = [4, 12, 'a', 'b', 5.0]
# Remove 'a'
alist.remove('a')
print('a' in alist)  # True if item is in the list
# Append data into list
alist.append(10)
# Insert data into list
alist.insert(1, -3)
print(alist)

# %% List (5)
s = 'Test 12!' 
# Convert string to list
t = list(s)
print(t)
# Convert list to string
u = ''.join(t)
print(u)

# %% List (6)
a = [1, 2, 3, 4]
b = a
print(b is a)
print(b == a)
a[1] = 0
print(a)
print(b)
print(id(a))
print(id(b))

# %% List (7)
a = [1, 2, 3, 4]
c = a[:]
print(c)
print(c == a)
print(c is a)
a.remove(2)
print(a)
print(c)
print(id(a))
print(id(c))

# %% Tuple (1)
empty_tuple = ()
t1 = (1)  # this is not a tuple
print(type(t1))
t2 = (1,) # this is a tuple with a single item
print(type(t2))
atuple = (7, 'abc', 3.142, [1.5, 2])
atuple[2] = -3

# %% Tuple (2)
from timeit import timeit
print(timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9, 0] '))
print(timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9, 0) '))

values = 1.23, -4.5  # packing
print(values, type(values))
a, b = values  # unpacking
print(a, b)
