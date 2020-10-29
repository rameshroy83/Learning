#!/usr/bin/python3

'''
This program is learning from chapter 8
this is related to how to use function in python

'''

def fac(num):
    fact =1
    for i in range(1,num+1):
        fact = fact * i
    return(fact)


num1 = int(input("Please enter the number to calculate factorial :"))
print(f"The factorial of {num1} is:",fac(num1))


# Here we created a function to build the factorial logic and later used it to compute the factorial.

