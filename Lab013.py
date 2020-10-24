#!/usr/bin/python3

'''
In this program we will discuss about the functions available for string manipulation.
'''

a = input("Please enter your name:")
print("The length of the sring entered above is:",len(a))
# The above function help us to calculate the length of the string.

# The next function help us to check if the string end with specific character or not
print("Does the string you entered with esh :", a.endswith("esh"))

# The next function will count the number of occurence of the specific character/word in the string

print("The number of time a occured in the above sring is",a.count("a"))

# Capitalise function is used to capitalise the first character of the string. Ramesh is ok

print("Capitalise statement on ramesh is ok",a.capitalize())

#the next find function will find and return the location of character or retur -1 if character no there.

print("The character a is located a indice location: ",a.find("a"))

# The next function is replace will find the occurance of the string and replace is with new

print("Replace name in Ramesh is Good", a.replace("Ramesh", "Suresh"))
