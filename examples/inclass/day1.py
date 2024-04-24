# In-class examples for Day 1

#%% Numeric data types
a = 29348759203498502793495829843759879432509328450829834729873923984092843
b = a ** 10
print(a, b, sep="\n")
print(a.__sizeof__())
print(b.__sizeof__())

c = 1234567890
d = 1_234_567_890
print(c, d, sep="\n")

#%% Binary and hexadecimal numbers
x = 0b10110101
y = 0x12cafe
print(x, y, sep=", ")
print(bin(x), hex(y), sep=", ")

#%% Variables

# class = 123  # Using keywords as variable name will cause syntax error

# type = 2  # Built-in functions can be shadowed by variables of the same name
# del type  # This will delete the varible

#%% Convert between different data types
a, b, c = 1, 2.3, '456'
print(type(a), type(b), type(c), sep=", ")

d, e, f = float(a), str(b), int(c)
print(type(d), type(e), type(f), sep=", ")

g = '123abc'
print(g, type(g), sep=": ")
h = int(g, 16)
print(h, hex(h), type(h), sep=": ")

#%% Type hinting
a: int = 123
b: float = 4.5

a = 'abc'  # Type hinting is not enforced by Python
c: str = 678  # Type hinting is not enforced by Python
print(a, b, c, sep=", ")

#%% Arithmetic operators
a = 3 ** 2
b = -3 ** 2
c = (-3) ** 2
print(a, b, c, sep=", ")

#%% Comparison operators
a = 10
b = 25
print(a < b)
print(a > b)
print(a == b)
print(a != b)

print(0 <= a < 100)
print(50 <= b < 150)

#%% Raw string
print("You can insert \n as the newline character.")
print(r"You can insert \n as the newline character.")
print("You can insert \\n as the newline character.")

#%% String indexing and slicing
s = "Introduction to Python"
print("First character: ", s[0])
print("Last character: ", s[-1])
print("First 12 characters: ", s[:12])
print("Last 6 characters: ", s[-6:])
print("Reversed string: ", s[::-1])

#%% String concatenation and repetition
a = '45'
b = '123'
c = a + b
print(a, b, c, sep=", ")

d = 10 * "Ha "
print(d)

#%% String methods
s = "Introduction to Python"
print(s.upper())
print(s.lower())
print(s.title())
print(s.replace('on', 'ami'))
print(s)  # s is not changed

t = s.upper().replace('N', 'M')  # methods can be chained
print(t)

#%% f-string formatting
a = 12.345
b = 0.05
c = 67890

print(f"{a = }, {a = :.0f}, {a = :.1f}, {a = :.2f}")

print(f"Percentage: {b:.2%}")

print(f"Binary: {c:b}, Hex: {c:08x}")

for i in range(1, 11):
    print(f"file{i:04}.txt")

#%% Getting input from the user
num = input("Enter an integer: ")

print(f"{num = }, {type(num) = }")

print(f"10 times of {num} is {10 * num}")

if num.isdigit():
    print(f"10 times of {num} is {10 * int(num)}")
else:
    print(f"{num} is not an integer!")

#%% List join, append and extend
alist = [1, 2, 3]
print(f"{alist = }")

alist = alist + [4]
print(f"{alist = }")

alist += [5]
print(f"{alist = }")

alist.append(6)
print(f"{alist = }")

alist.extend([7, 8])
print(f"{alist = }")

alist.append([9, 10])
print(f"{alist = }")

print(f"{len(alist) = }")

#%% Sorting list
blist = [3, 1, 4, 2, 6, 5, 0]
clist = sorted(blist)  # ascending
dlist = sorted(blist, reverse=True)  # descending
print(f"{blist = }, {clist = }, {dlist = }")

elist = blist.sort(reverse=True)  # descending
print(f"{blist = }, {elist = }")

#%% List methods
alist = [1, 2, 3.4, 'abc', [5, 6.78], 'yz', 1, 'a']

print(f"{alist.count(1) = }")
print(f"{alist.count('a') = }")
print(f"{alist.index(1) = }")  # only return the index of the first occurance

alist.remove(1)
print(f"{alist = }")  # only remove the first occurance of the item

alist.insert(2, 5)
print(f"{alist = }")

r = alist.pop(1)
print(f"{alist = }, {r = }")

#%% Tuple packing and unpacking
atuple = 1, 2.3, 4.5, 6
print(f"{atuple = }")

a, b, c, d = atuple
print(f"{a = }, {b = }, {c = }, {d = }")

x, *y = atuple
print(f"{x = }, {y =  }")

p, *q, r = atuple
print(f"{p = }, {q =  }, {r = }")


















