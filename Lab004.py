#!/usr/bin/python3

'''
This program has requirement to print the content of a directory via python OS module
going through the python module index we got to know that the 
os.listdir(path='.') function gives the directory content.

https://docs.python.org/3/py-modindex.html

The above url is handy to check the inbuilt modules of python and the details of the module and functions
within the module.
We can also use REPL test this function.

>>> os.listdir('/home/kali/Desktop/LAB/Learning/')
['Python Course with Notes', 'Lab004.py', 'Lab001.py', 'Lab003.py', 'README.md', '.git', 'Maroon_5_ft_Wiz_Khalifa_-_Payphone_Qoret.com.mp3', 'Lab002.py']
>>> 

'''
import os
print(os.listdir())
