# This file contains the samples codes for "Conditional Logic, Loop and Comprehension" section.

# %% Conditional Logic (1)
mark = 51
if mark >= 50:
    print("You passed the test!")
else:
    print("You failed the test!")

a = "Passed" if mark>=50 else "Failed"

# %% Conditional Logic (2)
mark = 51
if mark >= 70:
    print("You scored an 'A'!")
elif mark >= 60:
    print("You scored a 'B'!")
elif mark >= 50:
    print("You scored a 'C'!")
else:
    print("You failed the test!")

# %% Conditional Logic (3)
test1 = 60
test2 = 70
if test1 >= 50 and test2 >= 50:
	print("Passed both tests")
elif test1 >= 50 or test2 >=50:
	print("Pass one test")
else:
	print("Failed both tests")

# %% Conditional Logic (4)
gender, age = "F", 15
if gender == "M":
	if age > 12:
		discount = 5
	else:
		discount = 10
else:
	if age > 12:
		discount = 10
	else:
		discount = 15
print(f"Discount: {discount}%")

# %% Conditional Logic (6)
status_code = int(input("Enter status code: "))
match status_code:
	case 200:
		print("OK")
	case 404:
		print("Not Found")
	case _:
		print("Unknown status code")

# %% Loop (1)
range(5)		# 0, 1, 2, 3, 4
range(1, 11)	# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
range(2, 10, 2)	# 2, 4, 6, 8

# %% Loop (2)
for i in range(3):
    print(i)

alist = [1, 2.3, -4.5]
for i in alist:
    print(i + 1)

# %% Loop (3)
prices = {'apple': 1.5, 'orange': 2.5, 'pear': 4}
for k in prices:
	print(f'{k}: {prices[k]}')

# %% Loop (4)
fruits = ['apple', 'orange', 'pear']
prices = [1.5, 2.5, 4]
for i, j in zip(fruits, prices):
	print(f'{i}: RM {j:.2f}')

# %% Loop (5)
fruits = ['apple', 'orange', 'pear']
prices = [1.5, 2.5, 4]
for i, (j, k) in enumerate(zip(fruits, prices)):
	print(f' {i+1}. {j}: RM {k:.2f}')

# %% Loop (6)
for i in range(2):
    for j in range(3):
        print(f'Inner loop {j=}')
    print(f'Outer loop {i=}')
print('Outside of both loops')

# %% Loop (7)
i = 0
while i < 5:
    i += 2
    print(i)

# %% Loop (8)
bugs = ['bug 1', 'bug 2', 'bug 3']
while bugs:
	bug = bugs.pop(0)
	print(f"Fixing {bug}.")
print("All bugs fixed.")

# %% Loop (9)
for x in [0, 1, 2]:
	pass
if a > b:
	pass

# %% Loop (10)
for i in range(4):
	if i == 2:
	    break
	print(i)
print(f"Stopped at {i=}")

# %% Loop (11)
for i in range(4):
	if i == 2:
	    continue
	print(i)
print(f"Stopped at {i=}")

# %% List Comprehension (1)
squares = []
for i in range(1, 11):
	squares.append(i**2)

squares = [i**2 for i in range(1, 11)]

names = ['ali', 'bala', 'chan', 'david']
cap_names = [n.capitalize() for n in names]
print(cap_names)

# %% List Comprehension (2)
alist = ['Java', 'Rust', 'Python', 'Swift', 'Go']
filtered_list = [i for i in alist if 'o' in i]
print(filtered_list)

s = 'Testing 123! Are you there?'
t = [c if c.isalpha() else ' ' for c in s]
u = ''.join(t)
print(u)

# %% Dictionary Comprehention
days = ['Mon', 'Tue', 'Wed']
temps = [23.5, 25.7, 29.1]
days_temps = {k: v for k, v in zip(days, temps)}
print(days_temps)

d = {'Ali': 15, 'Baba': 21, 'Cloud': 35, 'Dave': 9}
d_adults = {k: d[k] for k in d if d[k] >= 18}
print(d_adults)