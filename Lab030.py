#!/usr/bin/pyton3

'''
This program is for the practice set chapter 8


'''



def greatest (num1, num2, num3):
    list1 = [num1, num2, num3]
    list1.sort()
    print(f"The greatest number is : ",list1[2])


num1 = int(input("Please enter the 1st number : "))
num2 = int(input("Please enter the 2st number : "))
num3 = int(input("Please enter the 3st number : "))

greatest(num1,num2,num3)
