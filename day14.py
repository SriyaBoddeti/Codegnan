'''
MODULES
---------
A module in a python is a file that contains python code such as
--> Variables
--> functions
--> classes
--> statements

two types of module
---------------------
1. user-define
===============
def add(a,b):
    return a+b
def sub(a,b):
    return a-b

2. built-in
=============
import math
print(math.sqrt(25))

print(math.factorial(4))

print(math.pow(2,5))

Eg: if we want to access only sqrt
from math import sqrt
print(sqrt(25))

      (or)
import math as m
print(m.sqrt(25))


--> os - it is used to communicate with the system
Eg: to create a folder in our system
import os
os.mkdir("python.txt")

Eg: to remove
import os
os.remove("python.txt")


--> sys -
import sys
print(sys.version)
print(sys.exit)
print(sys.path)

--> random - to get random numbers , used for otp
import random
print(random.randint(1000,99990))

--> Counter - to count no of frequencies in the data 
from collections import Counter
data = ['a','b','c','d']
counter = Counter(data)
print(counter)

-->defaultdict
from collections import Counter , defaultdict
data = ['a','b','c','d']
counter = Counter(data)
print(counter)

dd = defaultdict(int)
dd['missing'] += 1
print(dd['missing'])


'''



