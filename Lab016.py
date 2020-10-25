#!/usr/bin/python3

'''
In this program we will talk about list and Tuples
'''

a=[10,20,30,40,50]
print(a)

# as in string the list value starts from 0 to n-1

a[0] = 9
print(a)

b = [10, "Ramesh" , True, 5<4]
print(b)

#As in case for string indices we can do slicing for list as well.
print(b[0:2])

# We will 
#b.sort()
a.reverse()
print(a)
a.append("Haha")
print(a)
b.insert(3,"hahaa")
print(b)

# The append function will add the value at the end.
# the insert will add a value at specific location.
# The reverse and sort function as per name.

b.pop(3)
print(b)
a.remove("Haha")
print(a)

