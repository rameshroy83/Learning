#!/usr/bin/python3

'''
Snake Water Gun Game programmed against Computer

'''

import random

def Game(comp, user):
    if comp == user:
        return None
    elif user == 's':
        if comp == 'w':
            return True
        elif comp == 'g':
            return False
    elif user == 'w':
        if comp == 'g':
            return True
        elif comp == 's':
            return False
    elif user == 'g':
        if comp == 'w':
            return True
        elif comp == 's':
            return False         


num1 = random.randint(1,3)
if num1 == 1:
    comp = 's'
elif num1 == 2:
    comp = 'w'
else:
    comp = 'g'

user = input("Please enter your choice Snake (s), Water (w) or Gun (g)")
a = Game(comp,user)
print(f"You Choose : {user}")
print(f"Computer Choose : {comp}")

if a == None:
    print("The Game is a Tie")
elif a== True:
    print("You Won the Game!!")
else:
    print("You Lose the Game!!")
