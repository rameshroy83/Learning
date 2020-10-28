#!/usr/bin/pyton3

'''
This program is the practice set for chapter 7.
'''

num1 = int(input("Please enter the number :"))
t = 0

for i in range(1,num1+1):
    if num1%i==0:
        t +=1
         

if t<=2:
    print(f"The number {num1} is Prime")
else:
    print(f"The number {num1} is not Prime")

