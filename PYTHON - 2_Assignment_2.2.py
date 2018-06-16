# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 18:42:17 2018

@author: 1000091
Create the below pattern using nested for loop in Python.

"""
import os, sys

n=5

for i in range(n):
    for j in range(i):
        print ('*', end='')
    print('') 

for i in range(n,0,-1):
    for j in range(i):
        print('*', end='')
    print('')
