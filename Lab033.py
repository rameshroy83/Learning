#!/usr/bin/python3

'''
sum for first n natural numbers
'''

def sumnat(n):
    if n == 1:
        return 1
    else:
        return (n+sumnat(n-1))




print(sumnat(5))








