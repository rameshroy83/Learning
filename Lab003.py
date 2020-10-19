#!/usr/bin/python3

''' 
In this program we will use an external module by the name playsound and use it to play
a music file uploaded on the github directory

'''
import playsound
'''
The above method of importing the module help us use the module directly
Please note that this would involve downloading the playsound module via pip
pip install playsound, prior to that you should have pip intall on you machine.
Also note that when we use the file location in windows the location is usually backslash '\'
However the backslash is escape sequence in python thus you might have to use two backslash if file location
in windows like c:\\user\\home\\ etc.

'''
playsound.playsound('/home/kali/Desktop/LAB/Learning/Maroon_5_ft_Wiz_Khalifa_-_Payphone_Qoret.com.mp3')

