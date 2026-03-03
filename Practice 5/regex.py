import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)


import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)


import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)


import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)


import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)


import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)


import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object


import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())


import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)


import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

'''
RegEx Functions
The re module offers a set of functions that allows us to search a string for a match:

Function	Description
findall	Returns a list containing all matches
search	Returns a Match object if there is a match anywhere in the string
split	Returns a list where the string has been split at each match
sub	Replaces one or many matches with a string

'''