#!/usr/bin/python

'''
This program will include the programs practice list of Lesson 3.
'''

a = input("Please enter the string: ")
print("Hello", a)

template = '''
Dear <Name>,

We are please to inform you that you have been selected.

Regrads,
Teams
<Date>

'''
template = template.replace("<Name>", "Ramesh")
template = template.replace("<Date>", "25 Oct 2020")

print(template)


# Program to detect the occurance of double space in string.

c = input("Enter a long string with double spaces: ")
print(c.count("  "))


# Program to replace the double spaces with single space.

c=c.replace("  ", " ")
print(c)

letter = "Dear Harry,\n This Python Course is nice. \nThanks!"
print(letter)
