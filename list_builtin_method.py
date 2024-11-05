#count(): it is used for counting how many times given elements is repeated in list.
#syntax : count(value) here count does not take more tahn one arguments

l=[45,22,35,20,22,41,63,22,13]
print(l.count(22))

#index() : it is used for returning index position of given element of list .
#syntax: index(value,st,end)
print(l.index(22))
print(l.index(22,2,5))
#print(l.index(66))

#copy(): shallow copy
#it is used for copying only elements not the memory address.
# if we modify one variable another will not get modified.
#syntax : copy()
l1=l.copy()
print(l1)
print(id(l),id(l1))
del l[5]
print(l)
print(l1)
del l[1:4]
print(l)
del l[0:3]
print(l)
print(l1)

# = operator, deep copy:
#it is used for copying the both elements and memory address.
# if we modify one variable another will also get modified.
#syntax : =

l2=l1
print(l2)
del l1[1:5]
print(l1)
print(l2)

#clear(): it is used for removing all elements from given collection but not the memory address.
#syntax : clear()
l.clear()
print(l)

#insertion methods of list
#append(): it is used for adding the new element at the end of the list.
#single value data type or collection data type will be considered as one elemet.
#syntax : append(value)
l.append('hai')
print(l)
#l.append(5,6)
l.append((45,25))
l.append(5)
print(l) 

#extend(): it is used for extracting indivisual elements of given cdt then it will add them at end of the list.
#only cdt 
#syntax : extend(value)
l.extend([45,25,65])
print(l)
#l.extend(12,23)
l.extend((45,88,22,11))
print(l)

#insert(): it is used for adding the elements based on specified index position.
#if sepcified index position > len(cdt), then it will add them at the end of the list.
#single value data type and cdt considered as only one element.
#syntax : insert(index, value)
l.insert(3,'python')
print(l)
l.insert(0,55)
print(l)

#pop(): it is used for deleting the value based on specified index position.
#default value for pop() is -1 in list.
#if specified index postion is not there then pop will throw an error.

l=[1,2,3,4,5]
print(l.pop(2))
print(l)
print(l.pop())
print(l)
#l.pop(56) error out of index

#remove(): remove method is used for removing the element based on value, else it will throw an error.

print(l)
l.remove(4)
print(l)

# sort() : it is used for sorting the list in ascending order and descending order.
# varname.sort() for ascending
# varname.sort(reverse=True) for descending.

a=[45,12,965,25,25]
a.sort()
print(a)
a.sort(reverse=True)
print(a)


#which method return None in list.
#sort(), append(), extend(), insert(), remove(), clear().

# Builtin method of tuple :

#only count and index methods are same as that of list.

t=(45,56,45,12,23)
print(t.count(45))
print(t.index(45))
