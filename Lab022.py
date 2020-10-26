#!/usr/bin/python3

'''
This is a solution of practice set 6.
'''

num_1 = input("Enter the 1st number: ")
num_2 = input("Enter the 2st number: ")
num_3 = input("Enter the 3st number: ")
num_4 = input("Enter the 4st number: ")

if ((num_1 >= num_2) and (num_1 >= num_3) and (num_1 >= num_4)):
    {
        print("The greatest number is:",num_1)
    }
elif ((num_2 >= num_1) and (num_2 >= num_3) and (num_2 >= num_4)):
    {
        print("The greatest number is:",num_2)
    }
elif ((num_3 >= num_1) and (num_3 >= num_2) and (num_3 >= num_4)):
    {
        print("The greatest number is:",num_3)
    }
else:
    {
        print("The greatest number is:",num_4)
    }