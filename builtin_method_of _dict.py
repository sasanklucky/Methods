"""
Built-in method of Dictionary
==============================
"""
#keys(): it is used for getting all the keys of given dictionary.
var={'name':'sasank','age':25,'gender':'male'}
print(var)
print(var.keys())
print(type(var.keys()))

#values(): it is used for getting all the values of given dictionary.
var={'name':'sasank','age':25,'gender':'male'}
print(var.values())
print(type(var.values()))

#items(): it is used for getting all the items of given dictionary such as keys and values.
var={'name':'sasank','age':25,'gender':'male'}
print(var.items())
print(type(var.items()))

#copy(): perform shallow copy
d=var.copy()
print(d)
del d['name']
print(d)
print(var)

#clear(): remove all the elements from given dictionary and does not remove the memory address.
print(d)
d.clear()
print(d)

#get(): if specified key is present then get() will dispa-ly the value of specified key.else get() will display the default value.
#syntax : var.get(keys,default value) when you forget to give default value to keys then it eill return None as output.
var={'name':'sasank','age':25,'gender':'male'}
print(var.get('namee'))#None
print(var.get('name','Ravan'))
print(var.get('Sos','Rum')) # it will not update the dictionary
print(var)

#setdefault(): if specified keys is present then setdefault will display the value of specified keys.else setdefault 
#will update the dictionary with specified key and default value.
var={'name':'sasank','age':25,'gender':'male'}
print(var.setdefault('name','Ravan'))
print(var.setdefault('Sos','Rum'))
print(var)

#update(): it is used for updating the dictionary with multiple keys and value pairs at a time.
#it is used for merging the dictionary.
#if specified keys is present then update will update the value.
# if specified keys is not present then update will create new key and value in dictionary.
#syntax: varname.update({keys:values})
d={'name':'sasank'}
print(d)
d.update({'age':25,'gender':'male'})
print(d)

#pop(): it is used for reoving keys,value pair in dictionary based on specified keys.
#syntax: varname.pop(keys)
#if key is not present then it will throw an error.
d={'name':'sasank','age':25,'gender':'male'}
print(d.pop('age'))
print(d)
#print(d.pop('Namme'))

#popitem(): it is used for removing last key,value pairs in dictionary by default.
#syntax: varname.popitem()
d={'name':'sasank','age':25,'gender':'male'}
print(d.popitem())
print(d)
print(d.popitem())
print(d.popitem())
#print(d.popitem()) error bcz empty dict