'''
SETS
----
-->A set is collection of uique and unordered elements
-->Duplicate values are not allowed
-->Items  are not stored in index order
-->Represented in {}

any={1,2,3,4}
print(any)

o/p:{1, 2, 3, 4}


METHODS
-------
UNION()
-----
-->it will give all values from 2 sets together in once
syntax->variable_name.union(another variable)

any={1,2,2,3,4}
an={56,34}
print(any | an)
print(any.union(an))

o/p:{1, 2, 2, 3, 4, 34, 56}
    {1, 2, 2, 3, 4, 34, 56} 

INTERSECTION()
-------------
-->to get the common elements from both sides
syntax-->variable_name.intersection(another var)

any={1,2,2,3,4}
an={5,3,4,9,1}
print(any & an)
print(any.intersection(an))

o/p{1, 3, 4}
   {1, 3, 4}

DIFFERENCE
----------
-->to get the different values from the set
syntax-->variable_name.difference(another var)
'''

any={1,5,9,34,20}
an={5,7,3,1,6}
print(any - an)
print(an.difference(any))

o/p:{9, 34, 20}
    {3, 6, 7}

ADD()
---
-->to add new element into set
syntax-->variable_name.add(elements)
any={1,2,3,3,4}
any.add(41)
print(any)

UPDATE()
--------
-->to add multiple sets into set
syntax-->variable_name.update([element])
any={2,3,4,5,5}
any.update([41,60])
print(any)

any={2,3,4,5,5}
print(min(any))
print(sum(any))
print(len(any))

REMOVE()
-------
-->used to remove element from the set but it through error if element not in set
syntax-->variable_name.remove(element)
any={7,5,8,8,2}
any.remove(8)
print(any)


DISCARD()
--------
-->used to remove element from the set
any={7,5,8,8,2}
any.discard(8)
print(any)

'''
