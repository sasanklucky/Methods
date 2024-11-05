"""
 Built-in Method of Set
========================
"""
#copy(): performing shallow copy
a={78,89,45,56,12,23}
c=a.copy()
print(c)
#clear(): performing remove all the elements from set but not the memory.
c.clear()
print(c)

#add(): it is used for adding the element into a set in randomly.
a.add(55)
print(a)

#pop(): it is used for removing first element of set and it will not take any arguments.
print(a.pop())

#remove(): it is used for removing the element from set based on specified value.if the specified 
# value is not present it will throw an error.
a.remove(56)
#a.remove(59)
print(a)

#discard():
#it is used for removing the element from set based on specified value.if the specified value is not present it will not perform any operation.
a.discard(45)
a.discard(455)

#union(): it is used for getting all the element from the specified set.
b={12,45,67,89,90,23}
print(a)
print(a.union(b))

#intersection(): it is used for getting common elements from specified set.
print(a.intersection(b))

#difference(): it is used for getting the uncommon elements from the specified set.give the output based on baseset.
a={1,2,3,4}
b={3,4,5,6}
print(a.difference(b))

#symmetric_difference(): it is used for getting the uncommon elements from the specified set.
#it will give the output based on both sets.
a={1,2,3,4}
b={3,4,5,6}
print(a.symmetric_difference(b))

#update(): it is used for performing union operation and update the output into baseset.
a={1,2,3,4}
b={3,4,5,6}
a.update(b)
print(a)
a={1,2,3,4}

#intersection_update(): it is used for performing intersection operation and update the output into baseset.
a={1,2,3,4}
b={3,4,5,6}
a.intersection_update(b)
print(a)

#difference_update(): it is used for performing difference operation and update the output to base set.
a={1,2,3,4}
b={3,4,5,6}
a.difference_update(b)
print(a)

#symmetric_difference_update():
#it is used for performing symmetric difference operation and update the output to baseset.
a={1,2,3,4}
b={3,4,5,6}
a.symmetric_difference_update(b)
print(a)

#issupperset(): it used for returning True ,if elements of specified set should be present in base set.else return false.
a={1,2,3,4}
b={1,2,3,4,5,6}
print(b.issuperset(a))
print(a.issuperset(b))#b values should be present in set a.

#issubset(): it used for returning True ,if elements of baseset should be present in  specified set.
a={1,2,3}
b={1,2,3,4,5}
print(a.issubset(b))
print(b.issubset(a))

#isdisjoint(): it is used for returning True, if elements of specified set has uncommon element else return False.
a={1,2,3}
b={4,5,6}
print(a.isdisjoint(b))