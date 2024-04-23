# This file contains the samples codes for "String" section.

# %% String (1)
# using double quotes
a = "Hello"
# using single quotes
b = 'World'
print(type(a), type(b))

# %% String (2)
c = "How're you today?"
d = 'How\'re you today? ' # use esc char
e = '''A long string
that spans a few lines can be
enclosed in triple quotes.'''

s = 'lang\tver\Python\t3'
print(s)

t = r'lang\tver\Python\t3'
print(t)

# %% String (3)
s = 'apple pie'
print(s[0])  # first character
print(s[8])  # last character
print(s[-9]) # also first character
print(s[-1]) # also last character

# %% String (4)
s = 'apple pie'
print(s[9])    # index 9 is out of range

# %% String (4)
a = 'hello'
a[0] = 'c' # What happen if we change an item?

# %% String (5)
s = 'apple pie'
print(s[2:5])  # characters 2 to 4
print(s[:5])   # first 5 characters
print(s[-3:])  # last 3 characters
print(s[::-1]) # reverse string

# %% String (6)
s = 'Hello world!'
print(len(s))

a = 'Hello'
b = 'World'
print(a + b)

print('Hello' * 3)

# %% String (7)
a = 'Hello, World'
# Print all alphabets as uppercase
print(a.upper())

# Print all alphabets as lowercase
print(a.lower())

# To split the string by commas
print(a.split(','))

# %% String (9)
a, b = 6, 7.5
print('{} apples cost RM{:.2f}'.format(a, b))

a, b = 6, 7.5
print(f'{a} apples cost RM{b:.2f}')

# %% String (10)
val = "test"
print(f"Output: {val:10}")  # padded to 10 chars
print(f"Output: {val:>10}")	# align right
print(f"Output: {val:<10}")	# align left
print(f"Output: {val:^10}")	# align center
print(f"Output: {val:_>10}") # Use _ for padding

# %% String (11)
print("Area = " + chr(0x03c0) + "r" + chr(0x00b2))

print(f"Area = {0x03c0:c}r{0x00b2:c}")

print("I love to eat \N{sushi}")

# %% String (12)
x = input("Enter a number: ")
print(type(x))
print(x)
