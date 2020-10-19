#!/usr/bin/python3

#we again used shebang here we have already discussed about shebang in our Lab001
#In this lab we will talk about REPL, which basically is the IDE for the python. Lets use multiline comments to discuss on it.
'''
REPL: Stands for Read, Evaluate, Print, Loop. The REPL is how you interact with the Python Interpreter.
Unlike running a file containing Python code, in the REPL you can type commands and instantly see the output printed out. 
You can also use the REPL to print out help for methods and objects in Python, list out what methods are available, and much more.
like the dir(function/method name), type and help commands

>>> x='Ramesh'
>>> type(x)
<class 'str'>
>>> 

>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', 
'__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', 
'__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 
'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 
'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 
'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 
'swapcase', 'title', 'translate', 'upper', 'zfill']


As you can see the type returned the type of variable and the str method by itself has so many functions to it.
To get help on each function you can use the help

>>> help(swapcase)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'swapcase' is not defined
>>> help(str.swapcase)
Help on method_descriptor:

swapcase(self, /)
    Convert uppercase characters to lowercase and lowercase characters to uppercase.
(END)


note that we cannot use it directly as it is part of the str module we need to use object to refer to the module.

As discussed the REPL is very interactive.


Why we use REPL:
================
In this class, we’ll be working with a mix of the REPL and running code in files, like we’ll see in the next section. 
You’ll want to store code for reuse in files, while you can consider the REPL more of a scratch area. 
It’s the place where you can instantly play around and try out Python code. The REPL is a handy tool for both beginner and 
advanced Python programmers.

 '''
