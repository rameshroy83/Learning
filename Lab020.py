#!/usr/bin/python3

'''
In this program we will discuss about sets.
Sets are unordered list of items, these are not indexed and cannot be changed.
Also they cannot be duplicate.
'''

Set1 = {10,20,30,40}
Set2 = {10,60,70.90}

print(len(Set1))
# The above function prints the length of the set.

Set1.remove(30)
print(Set1)

# The above function removes a value from the set.

print(Set1.pop())
# The above function pop a value and return the value.

print(Set1)
Set3 = Set1.union({9,15})
print(Set3)
# The union functon add the value to the set items.

print(Set3)
Set4 = Set3.intersection({20,15,100})
print(Set4)
# The interset function only print the value common between both the sets.
