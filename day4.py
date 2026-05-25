'''
CONCATINATION
-------------
-->the(+) for int and can add, but for the other data types it will act as concatinating the data type
a=90
b=8
print(a+b)
any_="python"
so="is a launaguge"
print(any_+so)
an=[1,2]
am=[3,4]
print(an+am)

TUPLE
------
-->collection of different data types seperated by commas,represented in () and immutable

METHODS
-------
COUNT()
-------
---->this used to count the particular item in the tuple


syntax-->variable_name.count(item)

some=(1,"python",[1,2],(3,4))
print(some.count("python"))

INDEX()
------
--->used to find out the the index position of the item,and only gives the first occurance

some=(1,[1,2],(3,4),"python")
print(some.index("python"))

some=(2,[7,8],(90,7),"java","pandas")
print(some.index("java"))


DICTIONARY
----------
--->Dict is a key :value pair , key and value is seperated by : and pair is seperated by comma
eg:
sriya_details={"name":"sriya",
                1:2,
                (1,2):[3,4]}
print(type(sriya_details))

KEYS()
------
used to get keys from
syntax-->dict.keys()

sriya_details={"name":"sriya",
                "age" :21,
                "mobN":"123456789",
                "pan" :"KPXPB2072H"}
print(sriya_details.keys())

VALUES()
--------
sriya_details={"name":"sriya",
                "age" :21,
                "mob":"123456789",
                "pan" :"KPXPB2072H"}
print(sriya_details.values())

ITEMS()
-------
-->uesd to get key and value together
syntax-->dict.items()

sriya_details={"name":"sriya",
                "age" :21,
                "mob":"123456789",
                "pan" :"KPXPB2072H"}
print(sriya_details.items())


sriya_details={"name":"sriya",
                "age" :21,
                "mob":"123456789",
                "pan" :"KPXPB2072H"}
print(sriya_details.items())
print(sriya_details["age"])

UPDATE()
--------
-->used to add a new key :value pair into dict
synatx-->dict.update({key:value})

sriya_details={"name":"sriya",
                "age" :21,
                "mobN":"123456789",
                "pan" :"KPXPB2072H"}

sriya_details .update({"Aadhar":"967542345087"})
sriya_details['name']="boddeti"
print(sriya_details["age"])


sriya_details={"name":"sriya",
                "age" :21,
                "mobN":"123456789",
                "pan" :"KPXPB2072H"}

sriya_details .update({"Aadhar":"967542345087"})
sriya_details['name']="boddeti"
print(sriya_details)

CLEAR()
-------
-->used to remove all the items in the dict

sriya_details={"name":"sriya",
                "age" :21,
                "mobN":"123456789",
                "pan" :"KPXPB2072H"}
sriya_details.clear()
print(sriya_details)
'''





print(jyothi_details.keys())
