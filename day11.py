'''
BUILT-IN FUNCTIONS
---------------------
print() --> TO SEE THE O/P FOR THE PARTICULAR DATA TYPE
input() --> USER i/p
len()--> length of the element
type()--> datatype
max()--> maximum
min()-->minimum

sort-->sorted permanently
eg:m=[2,3,4,5]
m.sort()
print(m)
o/p: [2,3,4,5]

sorted-->only in the particular order

RECURSIVE FUNCTIONS
--------------------

--> a recursive function that calls itself to solve a program by breaking it into small or simple sub topics
Eg: factorial
def factorial(num):
    if num==1:
        return 1
    return num * factorial(num-1)
print(factorial(9))

Eg: even or odd using function
def even(num):
    if num % 2 == 0:
        print("EVEN")
    else:
        print("ODD")
even(9)

Eg: prime no using functions
def prime(num):
    for i in range(2, 101):
        for j in range(2, i):
            if i % j == 0:
               break
        else:
            print(i, "is prime")

prime(56)



return --> this ends a function execution and sends a value back to the code that is called a funvction
--------
eg: def add(a,b):
        return a+b
    res = add(4,5)
    print(res)



LAMBDA FUNCTIONS
-----------------
--> also called as single line functions 
--> small function
--> A lambda function is a small anonymous functions
--> syntax - lambda arguments : expression
Eg: using operator
so = lambda a,b,c: a+b+c+a
print(so(3,4,9))

Eg: using divisor
so = lambda a,b,c: b//a
print(so(3,4,9)

Eg: using power
power = lambda a, b: a ** b
print(power(2, 3))


'''




























