# This file contains the samples codes for "Functions" section.

#%% Functions (2)
def add_one(x):
	print(x+1)
add_one(5)

def add_two(x):
	return x+2
b = add_two(13)
print(b)

# %% Functions (3)
def myfunc(a, b, c=3):
	print(f'{a=}, {b=}, {c=}')
myfunc(1, 2, 3)
myfunc(4, 5)
myfunc(c=1, a=3, b=5)
myfunc(b=5, a=3)

# %% Functions (4)
# Mutable argument
def fun1(x):
	x.append('new')
	print(x)
a = ['old']
fun1(a)
print(a)

# Immutable argument
def fun2(y):
	y = 'new'
	print(y)
b = 'old'
fun2(b)
print(b)

# %% Functions (5)
def inventory(item, price, record = {}):
	record[item] = price
	return record
fruits = inventory('apple', 1.5)
fruits = inventory('pear', 3.5, fruits)
print(fruits)
stationaries = inventory('pen', 0.8)
print(stationaries)

# %% Functions (6)
def add_numbers(x: int, y: int) -> int:
    return x + y

def sum_num(nums: list[int]) -> int:
	return sum(nums)

# %% Functions (7)
def myfunc2(*arg):
	print(arg)
myfunc2(1, 2, 3)
myfunc2(4, 5, 6, 7, 8)

def myfunc3(**kwarg):
    for k in kwarg:
        print(f'{k} = {kwarg[k]}')
myfunc3(name='Ali', age=19, blood_type='O')

# %% Functions (8)
def ask_name():
    name = input('What is your name? ')
    if name:
        return name
    else:
        return ask_name()
print(f'Nice to meet you, {ask_name()}.')

# %% Functions (9)
def func():
	x = 2
	print(f"Inside 'func', x has the value {x}")
x = "Hello, World"
func()
print(f"Outside 'func', x has the value {x}")

#%% Functions (11)
def outer_func():
    a = 0.2
    y = 3
    def inner_func():
        a = 0.3
        z = 4
        print(f'Inside inner_func: {__name__=}, {a=}, {x=}, {y=}, {z=}')
    inner_func()
    print(f'Inside outer_func: {__name__=}, {a=}, {x=}, {y=}')
    try:
        print(f'{z=}')
    except NameError as e:
        print(f'Error: {e}')
a = 0.1
x = 2
outer_func()
print(f'Global: {__name__=}, {a=}, {x=}')
try:
    print(f'{y=}')
except NameError as e:
    print(f'Error: {e}')
try:
    print(f'{z=}')
except NameError as e:
    print(f'Error: {e}')

# %% Functions (12)
def myfunc4(a, b):
	'''This is a function to add two numbers'''
	return a + b
help(myfunc4)

# %% Functions (13 & 14)
def mygen():
	x = 0
	while x < 3:
		print(f'Generator: {x = }')
		yield x
		x += 1

for i in mygen():
	print(i)

# %% Functions (15)
def file_reader(file_name):
    for row in open(file_name, "r"):
        yield row

# %% Functions (16)
a = [ (1,2), (3,1), (5,10), (11,-3) ] 
print(sorted(a))
print(sorted(a, key=lambda x: x[1]))

# %% Functions (17)
# Find the square of 1 to 10:
sqr = list(map(lambda x: x*x, range(1, 11)))
print(sqr)
# Capitalize the first alphabet of each name:
names = ['ali', 'bala', 'chan', 'david']
cap_names = list(map(lambda x: x.capitalize(), names))
print(cap_names)

# %% Functions (18)
# Filter the array to get only odd numbers
even_nums = list(filter(lambda x: x%2, range(10)))
print(even_nums)
# Filter the list to get words start with vowels
words = ['bell', 'ant', 'cat', 'eggs', 'fish']
vowelWords = list(filter(lambda x: x[0] in 'aeiou', words))
print(vowelWords)
