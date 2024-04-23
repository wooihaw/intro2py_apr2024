# This file contains the samples codes for "Dictionary and Set" section.

# %%  Dictionary (1)
# Creating a dictionary with values assigned
a = {'a':'apple', 'c':'cat'}
# create an empty dictionary
b = {}

# %% Dictionary (2)
# Creating dictionary using {}
a = {'apple': 1.5, 'orange': 3, 'pear': 2.75}
# Creating dictionary using dict() function
b = dict(apple=1.5, orange=3, pear=2.75)
# Creating dictionary from two lists
k = ['apple', 'orange', 'pear']
v = [1.5, 3, 2.75]
c = dict(zip(k, v))

# %% Dictionary (3)
d = dict(apple=1.5, orange=3, pear=2.75)
print(d['apple']) # retrieve value via key
d['cherry'] = 9  # add a new key/value pair
print(d)
del d['orange']  # remove a key/value pair
print(d)
print('pear' in d) # check membership by key
print(2.75 in d)   # not by value

# %% Dictionary (4)
adict = {'apple':1.2, 'bread':2.8, 'candy':0.6}
# Return all keys in the dictionary
print(adict.keys())

# Return all values in the dictionary
print(adict.values())

# Get the value for 'apple'
print(adict.get('apple', 0))

# Remove the item with the key 'apple'
adict.pop('apple')
print(adict)

# %% Dictionary (6)
d = {'a':[1, 2], 'b':[3, 4]}
p = d
d['c'] = 5
print(d)
print(p)
q = d.copy()
q['x'] = 6
print(d)
print(p)
print(q)
d['b'].remove(3)
print(d)
print(p)
print(q)

# %% Dictionary (7)
from copy import deepcopy
d = {'a':[1, 2], 'b':[3, 4]}
r = deepcopy(d)
d['b'].remove(3)
print(d)
print(r)

# %% Set (1)
a = {1, 2.5, 'abc'}
print(type(a))

# %% Set (2)
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
s2 = {1, 3, 5, 7, 9}
s3 = {2, 4, 6, 8}
print(s1.intersection(s2))
print(s2.intersection(s3))
print(s2.union(s3))
print(s1.difference(s3))
print(s1 & s2) # s1.intersection(s2)
print(s2 & s3) # s2.intersection(s3)
print(s2 | s3) # s2.union(s3)
print(s1 - s3) # s1.difference(s3)
print(s1.issuperset(s2))
print(s3.issubset(s1))
print(s2.isdisjoint(s3))
