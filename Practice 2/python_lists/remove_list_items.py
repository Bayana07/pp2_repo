thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1) #remove second item
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop() #remove last item
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist #deletes list compeletely

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) #The list still remains, but it has no content.