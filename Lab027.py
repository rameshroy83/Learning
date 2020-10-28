#!/usr/bin/python3

'''
this is to solve the questions of practice set 7

'''

num1 = int(input("Enter the number: "))

fact = 1

for i in range(1,num1+1):
    fact = fact*i

print(f"The factorial of {num1} is :", fact)

