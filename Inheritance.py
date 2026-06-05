'''
Inheritance
-------------
--> This allows one class to acquire the properties and methods of another class .

Types
------
1.single Inheritance(father-child)
---------------------------------------
--> A class inherits from a single parent class.
-->eg1
class father:
    def land(self):
        print("I have 5A")

class sriya(father):
    def my_own(self):
        print("I have 2A")

fam = sriya()
fam.land()

--> eg2
class sriya:
    def dresses(self):
        print(" i ordered few dresses today ")

class deepu(sriya):
    def jewellary(self):
        print(" i brought new earings ")

fam_ = deepu()
fam_.dresses()
fam_.jewellary()

2.Multiple Inheritance (father,mother-child)
---------------------------------------------
--> A child classs inherited for more than one parent class.
class father:
    def land(self):
        print("my father have 5A")

class mother:
    def gold(self):
        print(" my mother have 1 kg gold ")

class sriya(father,mother):
    def mine(self):
        print("I have ntg")

fam_ = sriya()
fam_.land()
fam_.gold()

3. Multi_level Inheritance ( grandfather-father-child )
--------------------------------------------------------------
--> A class inherits from a parent class and another class inherits from that child class.
class grandfather:
    def land(self):
        print("my grandfather have 5A of land")

class father(grandfather):
    def flat(self):
        print("my father have flat at BNG")

class sriya(father):
    def mine(self):
        print("I have both of their property")

fam_ = sriya()
fam_.land()
fam_.flat()
fam_.mine()

4. Hierarchical Inheritance ( father - child,child )
------------------------------
--> Multiple child classes inherits from a single parent.
class father:
    def land(self):
        print(" 10A of land ")

class sriya(father):
    def mine(self):
        print(" job ")

class deepu(father):
    def sis(self):
        print(" student ")

fam_ = deepu()
fam_.land()

so_ = sriya()
so_.land()

-->eg2
class biriyani:
    def food(self):
        print(" chicken dum ")

class restaurant(biriyani):
    def mine(self):
        print(" juices ")

class home(biriyani):
    def sis(self):
        print(" snacks ")

fam_ = restaurant()
fam_.food()

so_ = home()
so_.food()


5. Hybrid Inheritance 
------------------------
--> This is the combination of two or more types of inheritance.
-->eg1
class A:
    def some(self):
        print('class A')

class B(A):
    def any(self):
        print('class B')

class C(A):
    def so(self):
        print('class c')

class D(B,C):
    def all(self):
        print('class D')

how = D()
how.so()
--------------------------------------------------------------------------------------------------------------

 super() METHOD 
------------------
--> super() is used to access methods and constructor of the parent class from the child class .
--> Eg1:-
class parent:
    def display(self):
        
        print('Method Parent')

class child(parent):
    def display(self):
        super().display()
        print('Method Child')

any_ = child()
any_.display()
-->Eg2:-
class person:
    def __init__(self,name):
        self.name = name

class stu(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll

    def show(self):
        print(f"Name : {self.name}")
        print(f"Roll No : {self.roll}")

any = stu('sriya',7)
any.show()
-------------------------------------------------------------------------------------------------------------
'''







