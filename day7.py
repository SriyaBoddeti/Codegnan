'''
F-string--> used for adding value to the string
 print(f"{num} is a number")


Statements-->
condition,control,loop
-------------------------

Condition
----------
if--> to check the statement true or not
eg: num=6
if num % 2 == 0:
    print(f"{num} is a even")
    
if-else--> else in the if statement, incase the condition becomes false then it will enter into flow-back(else),it will execute whatever inside it
eg: num=6
if num % 2 == 0:
    print(f"{num} is a even")
else:
    print(f"{num} is a odd")

eg: age=int(input("Enter your age: "))
if age>=18:
    print("you are eligible to vote")
else:
    print(f"we have to wait for {18-age} years")

eg:greatest number
num=8
num_2=15
if num>=num_2:
   print(f"{num}is a  greater number than {num_2}")
else:
   print(f"{num_2}is a  greater number than {num}")

eg:leap year
year = int(input("year= "))
if ( year % 4 == 0 and year % 100 != 0 ) or year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not  a leap year")

eg: is a vowel or consonent
vowel="s"
if vowel in "aeiouAEIOU":
    print(f"{vowel} is a vowel")
else:
    print(f"{vowel} is a consonent")

eg: positive or negative
num=int(input("Enter a number: "))
if num>=0:
    print(f"{num} is a positive number")
else:
    print(f"{num} is a negative number")

eg: pass or fail
marks = int(input("enter your marks: "))
stu_name = input("enter your name: ")

if marks >= 35:
    print(f"{stu_name} is passed")
else:
    print(f"{stu_name} is failed")

eg: divisibility rule
num=int(input("number: "))
if num%3 == 0 and num%5 ==0 :
    print(f"{num} is divisible")
else:
    print(f"{num} is not divisible")

eg: signal go or stop
Signal = input("Enter \n1.Red\n2.Green ")
if Signal == 1:
   print(f"{Signal} Go")
else:
   print(f"{Signal} stop")

nested if--->

elif

'''


