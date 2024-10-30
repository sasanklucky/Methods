"""
Functions
=========
Function is an independent block of code which is used for performing some specific task.

Methods
=======
Method is a function which is define inside a class.

Built-in method of string
==========================
Here, we are going to perform some operation on strings but we won't modify the actual value of string.


"""

#case conversion method 
#lower(): it is used for converting each and every elements of given string to lower case.
s='Developers'
print(s.lower())

#upper() : it is used for converting each and every elements of given string to upper case.
var="Nicky Joens"
print(var.upper())

#title() : it is used for converting the first charecter of each and every word of given string to upper case and 
# remaining charecter  to lower case.
s= "hay duDe! what's up "
print(s.title())

#capitalize() : Capitalize() is used for converting the first charecter of given string to upper case and remaining to lowercase.
string="sasank sekhar Baral"
print(string.capitalize())

#swapcase() : it is used for swapping all the lower case charecter to uppercase and uppercase to lower case.
v='Main Prem ki diwani hoon'
print(v.swapcase())

#islower(): it is used for returning True weather given string satishfy lower method else return False.
s='satish'
print(s.islower())
s='SASANK'
print(s.islower())
s='Sasank'
print(s.islower())

# isupper(): it is used for returning True weather given string satishfy upper method else return False.
s='satish'
print(s.isupper())
s='SASANK'
print(s.isupper())
s='Sasank'
print(s.isupper())

#istitle(): it is used for returning True weather given string satishfy title() else return False.
string="Sasank Sekhar Baral"
print(string.istitle())
string="Sasank Sekhar BARAL"
print(string.istitle())

#isalpha(): it is used for returning True weather given string contains only alphabates else return False.
string="Hey Sasank Are you Okey33"
print(string.isalpha())
string="Sasanksekharbaral"
print(string.isalpha())
string="Hey Sasank"
print(string.isalpha())

#isdigit(): it is used for returning True weather given string contains only digit else return False.
string="1234567890"
print(string.isdigit())
string="sasank's Pytho23n"
print(string.isdigit())

#isalnum(): it is used for returning True weather given string contains only alphabates, only digits and
#  combination of both else return False. 
string="Sasa5nk Sek522har Baral"
print(string.isalnum())
string="Sasank45Sekhar535Baral"
print(string.isalnum())
string="741262"
print(string.isalnum())
string="Developers"
print(string.isalnum())

#isspace(): it is used for returning True weather given sting contains only space else return False.
string="Sasank Sekhar Baral"
print(string.isspace())
string= " "
print(string.isspace())

#strip(): this method is used for removing leading space from given string.
#it is two types in python 
#lstrip(): it is used for removing left side space from given string.
#rstrip(): it is used for removing right side space from given string.
string="   Sasank Sekhar Baral   "
print(string.strip())
print(string.lstrip())
print(string.rstrip())
"""
>>> str=" sasank "
>>> str
' sasank '
>>> str.strip()
'sasank'
>>> str.rstrip()
' sasank'
>>> str.lstrip()
'sasank '
"""
#split(): it is used for spliting the given string based on given delimeter.
#syntax varneme.split(Delimeter,counts)
#default of given delimeter is space, default of count is how many given delimeters are repeated.
string="Sasank Sekhar Baral"
print(string.split())
print(string.split("s"))
print(string.split('S'))
print(string.split("S", 1))
print(string.split("a"))
print(string.split('a',3))
print('orange'.split('o',5))
print('orange'.split('s'))
# rsplit(): it is used for spliting given string based on direction (right to left <===========)
var="hai python"
print(var.rsplit('5'))
print(var.rsplit('h'))
print(var.rsplit('h',1))
var1='sos'
print(var1.split('s'))
print(var1.split('s',1))
print(var1.rsplit('s',1))

#replace(): it is used for replcaing the existing charecter with new charecter.
#syntax : varname.replace('existing chare','new chare',count)
#default for count is nomber of time given substring is repeared.
string="Sasank Sekhar Baral"
print(string.replace('S','W'))
print(string.replace('S','W',1))
print(string.replace('S','W',5))
print(string.replace('m','W'))
print(string.replace('S','v').replace('a','q'))

#count(): it is used for returning how many given substring is repeated in given string.
#syntax : varname.count('substring',starting index,ending index)
#default for starting index is 0, default for ending index is length of string.
string="Sasank Sekhar Baral"
print(string.count('a'))
print(string.count('a',2))
print(string.count('a',2,12))
print(string.count('w'))

#index(): it is used for returning index position if given value is present else it will throw an error.
#syntax : varname.index('value',starting index,ending index)
#direction  is left to right ========>
string="Sasank Sekhar Baral"
print(string.index('a'))
print(string.index('a',2))
print(string.index('a',2,12))#it will give first occurance
#print(string.index('w'))#it will throw an error

#rindex(): it is used for returning index position if given value is present else it will throw an error.
#syntax : varname.rindex('value',starting index,ending index)
#direction is right to left <===========
string="Sasank Sekhar Baral"
print(string.rindex('a'))
print(string.rindex('a',2))
print(string.rindex('a',0,12))#it will give first occurance from right to left
#print(string.rindex('w'))#it will throw an error

#find(): it is used for returning index position if given value is present else it will return -1 as output.
#syntax: varname.find('value',st index,en index)
#direction is left to right ======>
string="sasank sekhar baral"
print(string.find('a'))
print(string.find('a',2))
print(string.find('a',0,8))
print(string.find('w'))

#rfind(): it is used for returning index position if given value is present else it will return -1
#syntax: varname.rfind('value',st index,en index)
# direction is right to left <========

string='Developers'
print(string.rfind('e'))
print(string.rfind('e',0,5))  
print(string.rfind('k'))
print(string.rfind('e',81,0)) #invalid search index position
print(string.rfind('e',-10,-1)) 
#startswith(): this method is used for returning True if given string start with specified substring else return False.
#syntax : varname.startswith('substring',st index,End index)
string='ios user'
print(string.startswith('i'))
print(string.startswith('i',1))
print(string.startswith('io'))
print(string.startswith('io',1))

#endswith(): this method is used for returning True if given string ends with specified substring else return False.
#syntax : varname.endswith('substring',st index,End index)
string='ios user'
print(string.endswith('r'))
print(string.endswith('r',2))# bcz its st index position
print(string.endswith('r',2,5))
print(string.endswith('r',1,10))
print(string.endswith('er',6,10))
print(string.endswith('er',7,10))

#format(): it is used for creating dynamic string ,we need to create place holders.
#place holder are created by using {}.
#syntax: "contect{}".format(vslue1,value2)
#syntax: "contect{index}".format(value1,value2)
string="My name is {0} and my age is {1}"
print(string.format('Sasank','25'))
name='SASANK'
a=25
print(f'this is {name} and my age{a}.')
print(f"hii dude your{name}and your age{a}")

#join(): it is used for creating new string by joining the elements of given collection with glue charecter.
#syntax: glue charecter.join(collection)
# List of strings
words = ['Hello', 'world', 'from', 'Python']

# Join the words with a space as a separator
result = ' '.join(words)
print(result)  # Output: "Hello world from Python"

# Join the words with a comma as a separator
result_with_comma = ', '.join(words)
print(result_with_comma)  # Output: "Hello, world, from, Python"

# Join with no separator
result_no_separator = ''.join(words)
print(result_no_separator)  # Output: "HelloworldfromPython"

print('@'.join('sasank'))
