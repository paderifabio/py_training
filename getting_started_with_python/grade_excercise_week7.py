#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 16:55:53 2020

@author: fabiopaderi
"""

largest = None
smallest = None

while True:
    
    sval = input('Enter a value:')
    
    if sval == 'done': break
    
    try:
        intval = int(sval)
    except:
        print('Invalid input')
        continue
    
    if largest is None:
        largest = intval
    if smallest is None:
        smallest = intval
    
    if intval > largest:
        largest = intval
    
    if intval < smallest:
        smallest = intval
        

print('Maximum is',largest)
print('Minimum is', smallest)