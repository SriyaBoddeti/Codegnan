'''

List comprehension
-----------------------
--> List comprehension offers a shortest syntax when we want to create a new list from existing list
syntax--> vari_name = [expression loop condition]
--> example to print even in place of even no
old = [11,22,43,44,46]
new = [an if an%2!=0 else "even" for an in old]
print(new)

Generators
------------
-->Generators in python are a special type of iterable,allowing using to iterate over data efficiently without storing everything in memory...
-->They generate values lazily using yield keyword
-->Lazy Evolution
--> should call (next(gen)) to execute & more than the field print o/p & contains error says stop iteration 
def sample_gen():
    print("Start")
    yield 1
    yield 2
    yield 3
    print("end")
gen = sample_gen()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

o/p:
Start
1
2
3
end
Traceback (most recent call last):
  File "C:/Users/SRIYA/OneDrive/Desktop/codegnan/day13.py", line 30, in <module>
    print(next(gen))
StopIteration

why we use gen
----------------
--> Generators do not store the entire dataset in memory, they generate values on the fly a run time.
-->Avoiding unneccessary storage of data speed up execution.

How it works
--------------
-->It looks like normal function but uses the yield keyword instead of return
-->When the function is called, it does not execute immediately. Instead, it return a generator object which can be iterated using loop or the next() function.
def any(num):
    for i in range(num):
        yield i*i
a = any(6)
print(next(a))
print(next(a))

Eg: squares print
def sqr(num):
    result = []
    for i in range(1,num+1):
        result.append(i*i)
    return result
print(sqr(5))
o/p: [1, 4, 9, 16, 25]


Eg: to print only consonents and remove vowels
so = 'It looks like normal function but uses the yield keyword instead of return'
any = ''
for j in so:
    if j not in "AEIOUaeiou":
        any += j
print(any)

'''





