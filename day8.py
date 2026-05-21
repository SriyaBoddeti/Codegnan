'''
time_ ="23:32"
parts_ = time_.split(":")
print(f"{time} is converted into {int(parts_[0]) - 12} : [{parts_[1]} PM")

elif--> used to check more than 1 options
eg: Grades
stu_marks = int(input("Enter marks : "))
if stu_marks >= 90:
    print("A+")
elif stu_marks >= 80:
    print("A")
elif stu_marks >= 70:
    print("B+")
elif stu_marks >= 60:
    print("B")
elif stu_marks >=50:
    print("C+")
elif stu_marks >=35:
    print("Passed")
else:
    print("Failed")

eg: biggest number
a=8
b=57
c=89
if a > (b and c):
    print(a)
elif b > (a and c):
    print(b)
else:
    print(c)


nested if--->
eg:Bank pwd
SBI_bank = {"ATM PIN" : "6000"}
pin = input("enter 4 digit ATM pin : ")
if len(pin) == 4:
    if pin in SBI_bank['ATM PIN']:
        print("Welcome to SBI ATM")
    else:
        print("Invalid pin")
else:
    print("Pls enter 4 digit pin")

for statement--> used to iterate over a sequence
-------------------------------------------------
eg: any={1,2,3,4}
so={5,6,7,8}
an="python"
for i in any:
    print(i)

range() function ---> range is a in-built function used to generate numbers in sequencial manner
syntax: range(start,end,step)
eg:for i in range(1,100,4):
    print(i)

else in for ---> once the iterations completed this else will be executed 
eg: for i in range(1,100,4):
    print(i)
else:
    print("code ended here")

break---> used to exit from the loop based on the condition 
-------------------------------------------------------------

continue--> used to skip the current iteration based on the condition
eg: for i in range(1,10):
if i==3:
continue
print(i)

pass--> do nothing , Python requires indentation blocks after if, for, while, function, etc.
If you don't want to write code yet, use pass.
eg: for i in range(1,10):
    if i==3:
        pass



while loop --> until it satisfies the condition , for + if
eg: i = 1
while i>5:
    print(i)
    i += 1
-------------

'''








