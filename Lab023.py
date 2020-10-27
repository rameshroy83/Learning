#!/usr/bin/pyton3

'''
This program is part of the practice set 7

'''

Num1 = int(input("Please enter a number for which table you want to print : "))

for i in range(1,11):
    print(f"{Num1}*{i} = {Num1*i}")


Num2 = int(input("Please enter a number for which table you want to print : "))

i = int('1')
while i<=10:
    print(f"{Num2}*{i} = {Num2*i}")
    i+=1