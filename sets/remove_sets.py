thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
# output:{'apple', 'cherry'}

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
# output:{'apple', 'cherry'}

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(thisset)
# output:{'apple', 'cherry'}

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
# output:set()
