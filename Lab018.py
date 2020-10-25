#!/usr/bin/python3

'''
In this program we will solve the practice set for chapter4

'''

f1 = input("Enter the name for 1st fruit: ")
f2 = input("Enter the name for 2st fruit: ")
f3 = input("Enter the name for 3st fruit: ")
f4 = input("Enter the name for 4st fruit: ")
f5 = input("Enter the name for 5st fruit: ")

Fruit = [f1, f2, f3, f4, f5]
print("The list of fruits entered are: ", Fruit)


# Marks of 6 Students.

M1 = int(input("Enter the marks of 1st Student: "))
M2 = int(input("Enter the marks of 2st Student: "))
M3 = int(input("Enter the marks of 3st Student: "))
M4 = int(input("Enter the marks of 4st Student: "))
M5 = int(input("Enter the marks of 5st Student: "))

Marks = [M1, M2, M3, M4, M5]

print("The marks of students are as follow: ", Marks)
Marks.sort()
print("The marks in sorted order is :",Marks)




# Creating Tuple 

tupple = (1,2,3,4)
tupple[0] = 10
