'''
fibinocci series
-----------------
a=0
b=1
def fib(a,b):
    limit = int(input())
    print(a,b,end=" ")
    for i in range(1,limit):
        c = a+b
        a=b
        b=c
        print(c, end=" ")
fib(a,b)

---------------------------------
Eg: removing duplicates

an=[2,5,7,9,2,7]
num=[]
def duplicates(an,num):
     for i in an:
         if i not in num:
             num.append(i)
     print(num)
duplicates(an,num)

--------------------------------------
Eg : count the letters in a para
count = 0
so ="Artificial Intelligence"
def word(so,count):
    for j in so:
        count += 1
    print(count)
word(so,count)

-----------------------------------------
'''
