'''
TYPE CONVERSIONS
----------------
INT-->

an=78
us=str(an)
om=float(an)
print(om)
print(type(om))
print(type(us))

78.0
<class 'float'>
<class 'str'>

STR-->

an="90"
ear=list(an)
print(ear)
print(type(ear))
con=tuple(an)
print(con)

FLOAT-->

car=90.78
print(int(car))
print(type(str(car)))


LIST-->

any=[6,7]
print(str(any))
print(type(str(any)))
print(tuple(any))

TUPLE-->

how=(4,5)
print(list(how))
print(type(str(how)))

o/p:[4, 5]
    <class 'str'>
    
int as a user -input
---------------------
num=int(input("enter a number:"))
print(89+num)



str as a user -input
--------------------

some=input("write a text:")

list as a user input
--------------------
any=list(map(int,input("enter numbers:").split()))
print(any)         
             
o/p:enter numbers:4 6
    [4, 6]
 

tuple as a user input
----------------------

an=tuple(map(int,input("enter numbers:").split()))
print(an)

o/p:enter numbers:4 8
    (4, 8)

'''
num=eval(input("enter:"))
print(num)
