#!/usr/bin/python3

'''
This program is to program the practice set of chapter 9

'''

def game(score):
    print("Your Score for the Game is : ",score) 
    return(score)

# The function game is returning a score, now we have to built a logic if the score is overwitten or not.


def scoreupdate(score):
    f = open('Hiscore.txt','r')
    Hiscore = int(f.read())
    if int(Hiscore) > int(score) :
        None
    elif int(Hiscore) <= int(score) :
        f = open('Hiscore.txt','w')
        f.write(str(score))


score = int(input("Lets Play and Game and Enter Your Score : "))
game(score)
scoreupdate(score)
    


