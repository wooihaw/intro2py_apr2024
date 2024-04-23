# This file contains the samples codes for "File Operations" section.

# %% File Operations (3)
f = open("hello.txt", "r")
astring = f.read()
f.close()

with open("hello.txt", "r") as f:
    astring = f.read()

# %% File Operations (4)
with open('atext.txt', 'r') as f:
    astring = f.read() # including newline character

with open('atext.txt', 'r') as f:
	astring = f.read(10) # read the first 10 characters
	bstring = f.read(5)  # read the next 5 characters
	f.seek(0)  # go to the beginning of the file
	cstring = f.read(7)  # read the first 7 characters

# %% File Operations (5)
with open('atext.txt', 'r') as f:
	astring = f.readline()  # including newline character

with open('atext.txt', 'r') as f:
	alist = f.readlines() # including newline character

with open('utext.txt', 'r', encoding='utf-8') as f:
	ustring = f.read() # including newline character
print(ustring)

# %% File Operations (6)
astring = 'This is line 1'
with open('btext.txt', 'w') as f:
	f.write(astring) # newline character is not appended

alist = ['This is line 1\n', 'This is line 2\n', 'This is line 3\n']
with open('ctext.txt', 'w') as f:
	f.writelines(alist)  # newline character is not appended

# %% File Operations (8)
import pickle
a = ['a', 'b', 12.3, 4 -5j, [6, 7, 8.9]]
with open('mylist.pkl', 'bw') as f:
	pickle.dump(a, f)
with open('mylist.pkl', 'br') as f:
	b = pickle.load(f)

# %% File Operations (9)
import csv
temperatures = [
	[68, 65, 68, 70, 74, 72],
	[67, 67, 70, 72, 72, 70],
	[68, 70, 74, 76, 74, 73],
]
with open('temps.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerows(temperatures)

# %% File Operations (10)
import csv
temps = []
with open('temps.csv', 'r', newline='') as file:
	reader = csv.reader(file)
	for row in reader:
		# Convert row to list of integers
		int_row = [int(value) for value in row]
		# Append the list of integers to temps list
		temps.append(int_row)
print(temps)

# %% File Operations (11)
from urllib.request import urlopen
url = 'http://olympus.realpython.org/profiles/aphrodite'
with urlopen(url) as response:
	page = response.read()
print(page.decode('utf-8'))

# %% File Operations (12)
import gzip
s = '''How much wood would a woodchuck chuck if a woodchuck could chuck wood?He would chuck, he would, as much as he could, and chuck as much woodAs a woodchuck would if a woodchuck could chuck wood'''
t = gzip.compress(s.encode())  # encode to bytes
u = gzip.decompress(t).decode() # decode to string
print(len(s), len(t), len(u))

# %% File Operations (13)
import gzip
with open('lorem_ipsum.txt', 'r') as f:
	s = f.read()
	with gzip.open('lorem_ipsum.txt.gz', 'wb') as g:
		g.write(s.encode())

#%% File Operations (13)
import gzip
with gzip.open('lorem_ipsum.txt.gz', 'rb') as g:
	s = g.read().decode()  # decode to string
	with open('lorem_ipsum2.txt', 'w') as f:
		f.write(s)
