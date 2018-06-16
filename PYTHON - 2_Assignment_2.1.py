# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 18:42:17 2018

@author: 1000091

Write a program which accepts a sequence of comma-separated numbers from console
and generate a list.
"""
import os, sys

InString = input('Give sequence of comma-separated numbers:')
List = InString.split(',')
print(List)

