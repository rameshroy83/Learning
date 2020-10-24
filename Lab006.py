#!/usr/bin/python3

'''
This program we will talk about operator.
Arthimetic Operators: + - * / etc
'''

a = 123
b = 3
print(a+b)
print(a*b)
print(a-b)
print(a/b)

# Please note that the divide function always return a float datatype.

c = a/b
print(type(c))

'''
The other operators are assignment operators
'''

a=123
a+=2
print(a)

b = 123
b-=2
print(b)

c=3
c*=3

print(c)

d = 123
d/=3
print(d)

'''
Comparison operator used to compare two variables.
'''

a = (4>7)
print(a)

b = (4==7)
c = (4<=7)
d = (14!=7)


'''
Logical operators usually add boolean variable. Like and, or, not etc
'''

a= True
b= False

print (a and b)
print ( a or b)
print ( not a)

