#!/usr/bin/python3

'''
This program is about the lab practice exercise for lesson 5.

'''

Hindi_Dictionary = {
                        "Kitab" : "Book",
                        "Paani" : "Water",
                        "Seb"   : "Apple"

                    }

Word = input("Please enter the word you want to know the meaning of :")
print(f"The meaning of {Word} is", Hindi_Dictionary[Word])

num1 = input("Please enter the 1st number: ")
num2 = input("Please enter the 2st number: ")
num3 = input("Please enter the 3st number: ")
num4 = input("Please enter the 4st number: ")
num5 = input("Please enter the 5st number: ")

set = {num1, num2, num3, num4, num5}
print("The unique set of numbers is :", set.union({}))



Fruit = {
            "Raj" : "Apple",
            "Aman"  : "Banana",
            "Tina"  : "Apple",
            "Raj"   :  "Coconut",

}



print(Fruit["Raj"])

