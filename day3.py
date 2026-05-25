'''
any="python is a launguage"
print(any[::-2])

1.program to convert 24h clock into nrml clock


time_ =input ("enter 24 hours time: ")
parts_=time_.split(":")
hour_= int(parts[0])
min_= int(parts_[1])
print(f"{time_} is converted into{hour_ -12}:{min_} pm")


list
list is a collection of different data tyoes and represented in [] and seperated by ,
 --->it is mutable
 
any=[1,"python",[1,2]]
print(any)

     
any=[1,"python",[1,2,[34,"this is python 3rd class",78],"python is a launguage",89],34,[3,4]]
print(any[2][2])

o/p:[34, 'this is python 3rd class', 78]


append()

this method s used to add new item into list, and it will in the lastindex position
syntax-->variable_name.append(item)


any=[1,2,3]
any.append(6)
any.append([20,90])
print(any)

EXTEND
-->this method is used to add itterable into list,and it will in the last index position,each value or substring is each index in the list
syntax-->variable_name.extend(itterable)

--->IMMUTABLE                                         MUTABLE--> eg-list
    can able to modify on that particular variable
     eg-integer,string
    

so="python is a"
print(so.replace("python","java"))
print(so)
any=[1,2,3]
print(any.append(6))
print(any)


any=[1,2,3]
any.append("python")
any.extend([4,5])
print(any)


POP
--> used to remove the item from the list,but will mention here index position in the pop method
syntax-->variable_name.pop(index position)


any=[1,2,3]
any.pop
print(any)

o/p:[1, 2, 3]

any=[1,2,3]
any.pop(0)
print(any)

o/p:[2, 3]

REMOVE()
-->used to remove the item from the list,but will mention here direct in the remove method
syntax-->variable_name.remove()

so=["python",90,"java"]
so.remove("python")
print(so)

o/p:[90, 'java']


'''
any=[1,"python",[1,2,[34,"this is python 3rd class",78],"python is a launguage",89],34,[3,4]]
print(any[2][2])

o/p:[34, 'this is python 3rd class', 78]
