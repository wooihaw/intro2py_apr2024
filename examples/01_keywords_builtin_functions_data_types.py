# This file contains the samples codes for "Keywords, Built-in Functions and Data Types" section.

#%% Buiding Blocks
# This is a comment
import math as m

def greet(name):
    return f'Hello, {name}. Nice to meet you'

a = 2
b = 17.5
c = 'This is a string'

d = a + b

name = input('Please enter your name: ')
print(greet(name))

if a == 0:
    print('a is zero')
elif a > 0:
    print('a is positive')
else:
    print('a is negative')

for r in range(2, 5):
    area = m.pi * r ** 2
    print(f'Radius={r}, Area={area}')

# %% Container Data Types
alist = [57, 4.6, 'Hello', -7.5, 'world']

adict = {'name': 'Tan', 'age':45}

# %% Variables (1)
# assign the integer value 3 to variable a
a = 3
# assign the string 'Abc123' to variable b
b = 'Abc123'
# assign the list [1, 2.3, 'XyZ'] to variable c
c = [1, 2.3, 'XyZ']

# %% Variables (4)
my_variable: int = 10

# %% Variables (5)
a = 12
b = -3.45
c = 'Python'
print(a, b, c)
print(a, b, c, sep=',')
print(a, b, c, sep=':')

# %% Variables (6)
print('This is line 1.')
print('This is line 2.')
print('This is line 3.', end='')
print('This is still line 3.')

# %% Variables (7)
a, c, d = 12, -3.4, 5 + 6j
c, d = d, c

print(type(a))
print(type(c))
print(type(d))

a = 5
b = float(a)
c = str(a)
d = int(23.4)

# %% Operators and Expressions (4)
n = input("Enter a number: ")
while n != "quit":
    print(n)
    n = input("Enter a number: ")

while (n := input("Enter a number: ")) != "quit":
    print(n)
