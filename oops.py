'''
OOPs
------

1. class
-------------
--> A class is a blue-print or template used to create object.
Eg:
---
class stu_:
    name = 'sriya'
    
2. object
------------
--> An object is an instance of a class

Eg:
---
class stu_:
    name = 'sriya'

s1 = stu_()
print(s1.name)

Eg:
----
class stu_:
    def edu_(self):
        print("I am studing B.tech")
    def sports_(self):
        print("Cricket")
        print("Volly Ball")

s1 = stu_()
s1.edu_()


Attributes
------------
--> Attributes are the variables that belongs to a class or an object
Eg:
---
class stu_:
    name = 'sriya'
    age = 21

s1 = stu_()
print(s1.name)
print(s1.age)


Methods
--------
--> The functions defined inside the class is methods
Eg:
---
class PFS_DA:
    def python(self):
        batch_03 = 'PFS and DA'
        print('This is PFS and DA batch_03')

    def Flask(self):
        PFS = 'batch_03'
        print('This is DA batch_03')

all_ = PFS_DA()
all_.python()
all_.Flask()


Constructor - __init__
-----------------------------------------------------------------------------------------------
--> A constructor is a special method that is automatically called when an object is created.
Eg:
class ATM:
    def __init__(self,Balance,name):
        self.Balance = Balance
        self.name = name

    def Bal_check(self):
        print(f"{self.name} your total balance is {self.Balance + 500}")

    def name_(self):
        print(self.name)

card = ATM(Balance = 50000,name = 'sriya')
card.Bal_check()
card.name_()


Access Specifiers - way to pass attributes 
-------------------
1. Public
-----------
--> This can be accessed from anywhere in the program.
Eg:
---

2. Protected
-------------
--> This is represented using a single underscore(_)
Eg:
---
class stu_:
    _name = 'sriya'

s1 = stu_()
print(s1._name)

3. Private 
-------------
--> This is represented using a double underscore(__)
Eg:
--
class stu_:
    __name = 'sriya'

s1 = stu_()
print(s1.__name)

Encapsulation
--------------
--> Is the process of binding data and methods together

'''

class Bank:
    def __init__(self,balance):
        self.__balance = balance

    def depo_(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
acc = Bank(1000)
acc.depo_(10000)
print(acc.get_balance())
