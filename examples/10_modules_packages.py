# This file contains the samples codes for "Modules and Packages" section.

#%% Modules and Packages (4)
import math 
print(math.sin(math.pi/2))

import math as m 
print(m.sin(m.pi/2))

# %% Modules and Packages (5)
from random import randint
n = randint(1, 6)
print(n)

from random import choice
a = ['agree', 'neutral', 'disagree']
print(choice(a))

# %% Modules and Packages (6)
from random import shuffle
b = [1, 2, 3, 4, 5, 6]
shuffle(b)
print(b)

from random import normalvariate
print(normalvariate(0, 1))

#%% Modules and Packages (7)
from datetime import datetime as dt
current_datetime = dt.now()
print(current_datetime)

print(f"Today is {current_datetime:%d/%m/%Y}")
print(f"It's now {current_datetime:%H:%M:%S}")
print(f"It's now {current_datetime:%I:%M %p}")

#%% Modules and Packages (8)
from datetime import datetime as dt
start_date = dt(2000, 1, 1)
current_date = dt.now()
difference = current_date - start_date
print(f"Days passed: {difference.days}")

# %% Modules and Packages (9)
from random import randint
from collections import Counter
r = [randint(1, 6) for x in range(100)]
c = Counter(r)
print(c[3])	# print how many times 3 occurs
print(c.most_common(3))	# print the most common 3 items

# %% Modules and Packages (10)
from collections import namedtuple
Student = namedtuple('Student', ['name', 'age', 'DOB'])
peter = Student('Peter', '19', '2542003')
print(peter[1])	# Access using index
print(peter.name)	# Access using field name

# %% Modules and Packages (11)
import os
path = os.getcwd()
os.mkdir(os.path.join(path, "new_folder"))

# %% Modules and Packages (11)
import os
path = os.getcwd()
src = os.path.join(path, "new_folder")
dst = os.path.join(path, "old_folder")
os.rename(src, dst)

# %% Modules and Packages (12)
import os
path = os.getcwd()
os.rmdir(os.path.join(path, "old_folder"))

# %% Modules and Packages (12)
import os
os.startfile("lorem_ipsum.txt")

# %% Modules and Packages (12)
import os
path = os.path.join(os.getcwd(), "lorem_ipsum.txt")
print(os.path.exists(path))

# %% Modules and Packages (13)
import os
path = os.path.join(os.getcwd(), "new_folder")
print(os.path.isdir(path))

#%% Modules and Packages (13)
import os
path = os.path.join(os.getcwd(), "lorem_ipsum.txt")
print(os.path.isfile(path))

# %% Modules and Packages (14)
import os
path = os.getcwd()
for root, folders, files in os.walk(path):
	print(root)
	for folder in folders:
		print(folder)
	for file in files:
		print(file)

# %% Modules and Packages (17)
import sys
print(sys.path)

# %% Modules and Packages (18)
import adder
ans = adder.add(2, 3)
print(ans)

# %% Modules and Packages (21)
import mypackage.module1
import mypackage.module2
mypackage.module1.greet('Alibaba')
mypackage.module2.depart('Alibaba')
