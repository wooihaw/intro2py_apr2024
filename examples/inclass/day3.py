# In-class examples for Day 3

#%% Function and return value
def myfunc1(x, y):
    print(x, y)
    
def myfunc2(x: int|float, y: int|float) -> int|float:
    '''This is a function to add 2 arguments'''
    return x + y

a = myfunc1(11, 22)
b = myfunc2(33, 44)

print(f"{a = }, {b = }")

alist = [3, 1, 2, 5, 0]
blist =  sorted(alist)
clist = alist.sort()

print(alist, blist, clist, sep="\n")

#%% Function that returns multiple values
def myfunc3(x: int, y: int, z: int) -> tuple[int]:
    '''This is a function which returns 3 values'''
    return x*x, y*y, z*z

a = myfunc3(2, 3, 4)
print(f"{a = }, {type(a) = }")

b, c, d = myfunc3(5, 6, 7)
print(f"{b = }, {c = }, {d = }")

#%% Functions are objects
def func1(x: int) -> int:
    return x + 1

def func2(y: int) -> int:
    return y - 1

def func3(z: int) -> int:
    return z * 2

vals = [3, 4, 5]
functions = (func1, func2, func3)
for v in vals:
    for f in functions:
        print(f(v), end=' ')
    print("\n")


d_func1 = {'function 1': func1, 'function 2': func2, 'function 3': func3}
for k in d_func1:
    print(f"{k} returns {d_func1[k](10)}")

#%% Lambda function example 1
alist = [(1, 2, 3), (11, 4, 1), (7, 9, 2)]
blist = sorted(alist)
print(f"{alist = }\n{blist = }")

# To sort according to the 3rd element of each tuple in descending order
clist = sorted(alist, reverse=True, key=lambda x: x[2])
print(f"{clist = }")

#%% Lambda function example 2
# Sort the list based on the ID numbers
IDs = ['ID21', 'ID7', 'ID55', 'ID101', 'ID3', 'ID83', 'ID12', 'ID234', 'ID57']
print(f"{sorted(IDs) = }")

sorted_IDs = sorted(IDs, key=lambda x: int(x[2:]))
print(f"{sorted_IDs = }")

print(f"ID of oldest member: {min(IDs, key=lambda x: int(x[2:]))}")
print(f"ID of youngest member: {max(IDs, key=lambda x: int(x[2:]))}")

oldest, *others, youngest = sorted_IDs
print(f"{oldest = }, {youngest =}")

#%% lambda function example 3
GIDs = ['G2ID25', 'G1ID15', 'G2ID10', 'G1ID2', 'G2ID33', 'G1ID25', 'G2ID123']

print(f"{sorted(GIDs)}")

# Sort group in descending order and IDs in ascending order
sorted_GIDs = sorted(GIDs, key=lambda y: (-int(y[1]), int(y[4:])))
print(f"{sorted_GIDs = }")

#%% Example of map() function
# Reverse each string in a list
words = ['apple', 'bell', 'cat', 'door', 'eggs']

# Method 1 - Use for loop
r1 = []
for w in words:
    r1.append(w[::-1])
print(f"{r1 = }")

# Method 2 - List comprehension
r2 = [w[::-1] for w in words]
print(f"{r2 = }")

# Method 3 - Use map() function with lambda expression
r3 = list(map(lambda w: w[::-1], words))
print(f"{r3 = }")

#%% Example of filter() function
# Select only the palindrome from the tuple
words = ('ant', 'boy', 'civic', 'dad', 'mom', 'fish', 'madam')

# Method 1 - Use for loop
p1 = []
for w in words:
    if w == w[::-1]:
        p1.append(w)
print(f"{p1 = }")        

# Method 2 - List comprehension
p2 = [w for w in words if w == w[::-1]]
print(f"{p2 = }")

# Method 3 - Use filter() function with lambda expression
p3 = list(filter(lambda w: w == w[::-1], words))
print(f"{p3 = }")

#%% Combine map() and filter() functions
# Generate a list with the square of even numbers from 1 to 100 (inclusive)

# Method 1 - Use map() and filter() functions
sqr1 = list(map(lambda x: x*x, filter(lambda y: y%2==0, range(1, 101))))
print(f"{sqr1 = }")

# Method 2 - Use list comprehension
sqr2 = [x*x for x in range(1, 101) if x%2==0]
print(f"{sqr2 = }")

#%% Use lists and functions to keep books for library
def add_book(library, book):
    library.append(book)
    return library

def remove_book(library, book):
    if book in library:
        library.remove(book)
    return library

library1 = []
library1 = add_book(library1, "Harry Porter and the Goblet of Fire")
library1 = add_book(library1, "Harry Porter and the Deathly Hallows")
library1 = add_book(library1, "Fantastic Beasts")
print(library1)

library1 = remove_book(library1, "Fantastic Beasts")
print(library1)

library2 = []
library2 = add_book(library2, "Physics")
library2 = add_book(library2, "Chemistry")
library2 = add_book(library2, "Biology")
print(library2)

#%% Use OOP approach
class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            
    def __str__(self):
        return f"This is a library with {len(self.books)} books."

library1 = Library()
library1.add_book("Introduction to Python")
library1.add_book("Machine Learning with Python")
library1.add_book("Deep Learning Fundamentals")
print(library1.books)
print(library1)

library1.remove_book("Introduction to Python")
print(library1.books)
print(library1)

#%% OOP Example
class Rectangle:
    desc = "This is a rectangle"
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def __str__(self):
        return f"A {self.length} x {self.width} rectangle."
    def __repr__(self):
        return f"Rectangle({self.length}, {self.width})"
    def __gt__(self, other):
        return self.area() > other.area()
    def __eq__(self, other):
        return self.area() == other.area()
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2*self.length + 2*self.width
    
r1 = Rectangle(2, 3)
r2 = Rectangle(3, 2)
r3 = Rectangle(4, 5)

print(f"{r1}, {r1.area()}, {r1.perimeter()}")

rlist = [r1, r2, r3]
for i, r in enumerate(rlist, start=1):
    print(f"Rectangle {i}: {r.area()}, {r.perimeter()}")
    
print(rlist)

if r1 > r3:
    print("r1 is larger than r3")
else:
    print("r1 is smaller than r3")
    
if r1 == r2:
    print("r1 is the same size as r2")
else:
    print("r1 is not the same size as r2")

# Child class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
    def __str__(self):
        return f"A {self.length} x {self.width} square"
    def __repr__(self):
        return f"Square({self.length})"
    
s1 = Square(5)
s2 = Square(7)

print(s1, s2, sep="\n")

slist = [s1, s2]
print(slist)
for i, s in enumerate(slist, start=1):
    print(f"Square {i}: {s.area()}, {s.perimeter()}")

if s2 > s1:
    print("s2 is larger than s1")
else:
    print("s2 is smaller than s1")
    


    






















