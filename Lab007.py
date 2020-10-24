#/usr/bin/python3

'''
In this lab we will study about type casting, basically this is used to assin a datatye to the variable.
As we saw in the previous lab python is good at identifying the variable datatype, however
sometimes it might be that you want to assign an exception for the default python defination.
'''

a = 'Ramesh'
#b = int(a)
#print(b)

# Here we saw that we tried to convert a string to integer, however python was not able to as there is
# no logic behind converting a name to integer

a = '123'
b = '456'

print (a+b)

# above we saw that since we declared a and b in quotes python took it as string and when adding it,
# it did concatenation as expected, however how about we want to add it as number , then we need to
# convert it as integer.

print(int(a) + int(b))


