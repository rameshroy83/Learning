#!/usr/bin/python3

'''
Chapter 3 on Stings

'''

a = input("Enter your name:")
print("Good Morning",a)

print(a[0])  # This would print the first character of your input.
print(a[0:4]) # This would be first 4 character of your inputer 0,1,2,3 i.e 4-1.
# Note that the character numbering always starts from 0.

print(a[:4]) # if you dont enter the starting , then it would automatically start from 0.
print(a[0:]) # if you dont enter the ending, then it would automatically end till the last character.
print(a[-1]) # this would always print the last character, and you can sometimes use the negative indices
# as well to print the character of the string.

print(a[-4:-1]) # this would print the last three character like
# R     A       M       E       S       H
#-6     -5      -4      -3      -2      -1

print(a[0:5:2]) # The last number defines skip value, i.e it will skip every second character.
# Ramesh will be printed as RMS