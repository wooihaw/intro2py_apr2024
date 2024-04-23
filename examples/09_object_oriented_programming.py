# This file contains the samples codes for "Object-oriented Programming" section.

#%% Object-oriented Programming (2 & 3)
class Cat:
    pass

kilo = Cat()
print(type(kilo))

# %% Object-oriented Programming (3)
class Cat:
    def __init__(self, name, age):
            self.name = name
            self.age = age

# %% Object-oriented Programming (4)
class Cat:
    # Class Attribute
    species = "Felis catus"
    def __init__(self, name, age):
        self.name = name
        self.age = age

# %% Object-oriented Programming (5)
class Cat:
    species = "Felis catus"
    def __init__(self, name, age):
        self.name = name
        self.age = age

lilo = Cat("Lilo", 1)
milo = Cat("Milo", 2)
print(lilo.name)
print(milo.species)
milo.age = 4
print(milo.age)

# %% Object-oriented Programming (6 & 7)
class Cat:
    species = "Felis catus"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Instance methods
    def description(self):
        return f"{self.name} is {self.age} years old"
    def speak(self):
        return f"{self.name} says meow" 

kiko = Cat("Kiko", 3)
print(kiko.description())
print(kiko.speak())

print(kiko)

# %% Object-oriented Programming (7 & 8)
class Cat:
    species = "Felis catus"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def speak(self):
        return f"{self.name} says meow"

kiko = Cat("Kiko", 3)
print(kiko)

# %% Object-oriented Programming (9 & 10)
class Cat:
    species = "Felis catus"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def speak(self):
        return f"{self.name} says meow"
# Child classes
class Snowshoe(Cat):
	def speak(self):
		return f"{self.name} says hiss"
class Bengal(Cat):
	def speak(self):
		return f"{self.name} says purr"

kiko = Cat("Kiko", 3)
lilo = Snowshoe("Lilo", 1)
milo = Bengal("Milo", 2)
print(kiko)
print(lilo)
print(milo)
print(kiko.speak())
print(lilo.speak())
print(milo.speak())

# %% Object-oriented Programming (11)
print(isinstance(lilo, Cat))
print(isinstance(lilo, Snowshoe))
print(isinstance(lilo, Bengal))
print(getattr(kiko, 'name')) # same as print(kiko.name)
setattr(kiko, 'age', 4) # same as kiko.age = 4
delattr(kiko, 'age')    # delete age attribute of kiko
print(kiko.age)

#%% Object-oriented Programming (13)
mytuple = ("apple", "orange", "pear")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
