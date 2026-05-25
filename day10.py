'''
ASSERT KEYWORD
------------------

assert - debugging statement used to check the condition is true
eg: num=10
assert num < 5 
print("true")
output:
Traceback (most recent call last):
  File "C:/Users/SRIYA/OneDrive/Desktop/codegnan/day10.py", line 11, in <module>
    assert num < 5
AssertionError

eg:eligibility vote
age = 19
assert age >= 18
print("eligibile")


FUNCTIONS - used for more compatabilities  
---------------

--> A function is a block of code which only executes when it is called
--> We can pass data known as parameters into a function
--> To avoid repeated lines in code

def function_name(parameters):    #this is definition of the function
    -----
    -----
    -----
function_name(arguments)    #calling function 

eg: num = 9
def even(num):
    print(num)
even(num)

Eg: even or odd
num = 9
def even(num):
    if num % 2 == 0:
        print(f"{num} is even ")
    else:
        print(f"{num} is odd ")
even(num)
even(109)

ways to pass arguments
------------------------
1.required arguments - a function must be called with the same no of arguments
eg:num = 9
def even(num,num_2):
    if num % 2 == 0:
        print(f"{num} is even ")
    else:
        print(f"{num} is odd ")
even(109,90)
output:
109 is odd

eg: num = 9
def even(num,num_2,num_3):
    if num % 2 == 0:
        print(f"{num} is even ")
    else:
        print(f"{num} is odd ")
even(109,90)
output:
Traceback (most recent call last):
  File "C:/Users/SRIYA/OneDrive/Desktop/codegnan/day10.py", line 68, in <module>
    even(109,90)
TypeError: even() missing 1 required positional argument: 'num_3'


2.default arguments - By default , values is defined at parameters even throw it will take from arguments 
eg:def even(name="teja",age=89,sal=10):
    print(name)
    print(age)
    print(sal)

even("deepu",89,78)
output:
deepu
89
78


KEYWORD  ARGUMENTS
---------------------

--> we can send arguments with key=value syntax. By this,the order of arguments does not matter...
eg:def even(age,name,sal):
    print(name)
    print(age)
    print(sal)
even(name="sriya",age=21,sal=79000)
output:
sriya
21
79000


VARIABLE LENGTH ARGUMENTS
--------------------------

--> Adulting a star(*) before the parameter name in the function , receive a tuple of arguments and can access items with indexes 
EG: def even(*name):
    print(name[1])

even("SRIYA","DEEPU","SONY")
OUTPUT: DEEPU

Eg: name="sriya"
def even(any):
    print(any)
even(name)
OUTPUT: sriya


'''























































