'''
Nested Loops-->loop inside the loop
eg:for i in range (1,5):
    for j in range(1,2):
        print(i)
        print(j)

eg: tables
------------
num = int(input())
for j in range (1,11):
        print(f"{num} * {j} = {j*num}")

eg: reverse a string
----------------------
print(empty_str)

eg: palindrome
-----------------
so = input()
empty_str = ""
for j in so:
    empty_str == j + empty_str
if empty_str == so:
    print(f"{so} is palindrome")
else:
    print(f"{so} is not a palindrome") 

eg: amstrong
-------------
num=int(input())
amstrong = 0
length = len(str(num))
for i in str(num):
    amstrong += int(i) ** length
if amstrong == num:
    print(f"{num} is a amstrong number")
else:
    print(f"{num} is not a amstrong number")

eg: perfect number
------------------
num=int(input())
per_no = 0
for j in range(1,num):
    if num % j == 0:
        per_no += j
if per_no ==num:
    print(f"{num} is a perfect no")
else:
    print(f"{num} is not a perfect no")

eg: prime no
--------------
num=int(input())
count = 0
for k in range(1,num+1):
    if num % k ==0:
        count += 1
if count == 2:
    print(f"{num} is a prime no")
else:
    print(f"{num} is not a prime no")

--------------------
*
**
***
****
*****

star = 5
for g in range(1,star+1):
    for i in range(1,g+1):
        print("*" , end="")
    print()-->to print the output 

--------------------------------
A 
A B 
A B C 
A B C D 
A B C D E

star = 5
for i in range(1,star+1):
    for j in range(1,i+1):
        print(chr(64+j), end=" ")
    print()

---------------------------------
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

star = 5
count = 0
for i in range(1,star+1):
    for j in range(1,i+1):
        count += 1
        print(j, end=" ")
    print()

---------------------------------
* * * * * 
* * * * 
* * * 
* * 
*

star = 5
count = 0
for i in range(star,0,-1):
    for j in range(1,i+1):
        count += 1
        print("*", end=" ")
    print()

-------------------------------
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1 
0

star = 5
count = 0
for i in range(star,0,-1):
    for j in range(i):
        count += 1
        print(j, end=" ")
    print()

----------------------------
    * 
   * * 
  * * * 
 * * * * 
* * * * *

num = 5
for i in range(1,num+1):
    print(" "*(num-i), end="")
    for j in range(1,i+1):
        print("*", end=" ")
    print()

------------------------------
'''

























