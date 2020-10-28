#!/usr/bin/python3

'''
This program is code the practice set questions of chapter 7
'''

num1 = int(input("Enter the number n here and I will print the sum of first n numbers :"))
sum1 = 0

while num1>=0:
    sum1 = sum1 + num1
    num1 = num1 - 1

print("The sum is :", sum1)
