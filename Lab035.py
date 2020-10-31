#!/usr/bin/python3

'''
how to read and edit files via python
'''

f = open('sample.txt', 'r')
data = f.read()
print(data)
f.close()