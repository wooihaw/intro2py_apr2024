# In-class examples for Day 2

#%% Dictionary creation and modification
adict = dict(a=1, b=2.5, c='abc')
print(f"{adict['b'] = }")

adict['a'] = 3.45
print(f"{adict = }")

adict['d'] = [1, 2, 3]
print(f"{adict = }")

del adict['c']
print(f"{adict = }")

#%% Dictionary methods
adict = dict(a=1, b=2.5, c='abc')

# print(f"{adict['d'] = }")  # KeyError as the key is not in the dictionary adict

# Use get() method to return the default value of the key is not found
print(f"{adict.get('d', 0) = }")
print(f"{adict = }")

# Use setdefault() method to insert the key and default value if the key is not found
print(f"{adict.setdefault('d', 0) = }")
print(f"{adict = }")

#%% Joining two dictionaries
d1 = {'a':1, 'b': 2, 'c': 3}
d2 = dict(x=4, y=5, z=6)

# Method 1
d3 = d1.copy()
d3.update(d2)
print(f"{d3 = }")

# Method 2
d4 = d1 | d2
print(f"{d4 = }")

#%% Set methods
alist = [1, 2, 1, 3, 4, 5, 2, 1, 6]
aset = set(alist)
print(f"{aset = }")

name1 = ['Ali', 'Baba', 'Cloud', 'Data', 'Edward']
name2 = ['John', 'Donald', 'Edward', 'Peter', 'Ali', 'Chan']

# Names appear in both lists
common_names = set(name1) & set(name2)
print(f"{common_names = }")

# Names appear in only one of the lists
uncommon_names = set(name1).symmetric_difference(set(name2))
print(f"{uncommon_names = }")

# All the names in both lists
all_names = sorted(set(name1) | set(name2))  # sort the names in ascending order
print(f"{all_names = }")

#%% Conditional statement
mark = 45
if mark >= 50:
    print("Passed the test.")
    print("Still passed the test.")
    print("Passed the test again.")
else:
    print("Failed the test.")
    print("Still failed the test.")
    print("Failed the test again.")
print("Outside of the if-else block")

#%% Ternary expression
num = int(input("Enter an integer: "))

# Use if-else statement
if num % 2:
    print("This is an odd number")
else:
    print("This is an even number")
    
# Use ternary expression
print(f"This ia an {'odd' if num % 2 else 'even'} number")

#%% Examples for loop
names = ['ali', 'baba', 'cloud']
ages = [13, 37, 45, 53]
blood_types = ['a', 'o', 'b', 'ab', 'o']

# Use index to loop through multiple lists
for i in range(len(names)):
    print(f"{names[i]} is {ages[i]} years old with blood type {blood_types[i]}")

# Use zip() to combine multiple lists
for i, j, k in zip(names, ages, blood_types):
    print(f"{i} is {j} years old with blood type {k}")
    
# Use enumerate() to automatically add an index to each iteration
for n, (i, j, k) in enumerate(zip(names, ages, blood_types), start=1):
    print(f"{n}. {i.capitalize()} is {j} years old with blood type {k.upper()}")

#%% Example for while loop

while True:
    name = input("Enter your name: ")
    print(f"Hello {name}")
    ...
    ans = input("Do you want to repeat? (y/[n]) ") or 'n'
    if ans in ('y', 'Y'):
        continue
    elif ans in ('n', 'N'):
        print("Good bye and see you next time!")
    else:
        print("Invalid choice!")
    break

#%% List comprehension example 1
# Select the words that start with vowels
words = ('ant', 'boy', 'eggs', 'cake', 'door', 'house', 'owl')

# Method 1 - Use for loop
vowel_words1 = []
for w in words:
    if w[0] in 'aeiou':
        vowel_words1.append(w)
print(f"{vowel_words1 = }")

# Method 2 - Use list comprehension
vowel_words2 = [w for w in words if w[0] in 'aeiou']
print(f"{vowel_words2 = }")

#%% List comprehension example 2
# Calculate the number of odd numbers in a list
numbers = [1, 4, 3, 2, 5, 10, 11, 45, 32, 23, 57, 99, 72]

# Method 1 - Use for loop
count = 0
for n in numbers:
    if n % 2:
        count += 1
print(f"There are {count} odd numbers in the list.")        

# Method 2 - Use list comprehension
count2 = sum([n % 2 for n in numbers])
print(f"There are {count2} odd numbers in the list.")

#%% Dictionary comprehension
# Create a new dictionary for discounted price (after 10% discount)

prices = dict(apple=1.5, orange=3, durian=30, mango=12)

# Method 1 - Use for loop
new_prices = {}
for k in prices:
    new_prices[k] = 0.9 * prices[k]
print(f"{new_prices = }")

# Method 2 - Use dictionary comprehension
new_prices2 = {k: 0.9*prices[k] for k in prices}
print(f"{new_prices2 = }")

#%% Use any() and all() function
# Check whether any words in the list starts with a vowel
alist = ['bees', 'cats', 'eggs', 'boy']

# Method 1 - Use for loop
ans = False
for w in alist:
    if w[0] in 'aeiou':
        ans = True
        break
if ans:
    print("There is at least one word that starts with a vowel.")
else:
    print("There is no word that starts with a vowel.")

# Method 2 - Use any() and list comprehension
if any([True if w[0] in 'aeiou' else False for w in alist]):
    print("There is at least one word that starts with a vowel.")
else:
    print("There is no word that starts with a vowel.")

# Check whether all words in a list starts with a vowel
blist = ['apple', 'egg', 'owl']
if all([True if w[0] in 'aeiou' else False for w in blist]):
    print("All words start with a vowel.")
else:
    print("Not all words start with a vowel.")

#%% Use pickle to store a dictionary to a file
import pickle

data = {}
while (ans :=  input("Do you want to enter data? (y/n)")) in ('y', 'Y'):
    name = input("Enter name: ")
    age = input("Enter age: ")
    data[name] = age
print(f"{data = }")

with open("nameage.pkl", "wb") as f:
    pickle.dump(data, f)
    
#%% Use pickle to retrieve the saved dictionary from file
import pickle

with open("nameage.pkl", "rb") as f:
    mydata = pickle.load(f)
    
print(f"{mydata = }")

#%% Exception handling
while True:
    try:
        num = int(input("Enter an integer: "))
    except Exception as e:
        print("Error:", e)
    else:
        print(f"You have entered {num}.")
        break
    















