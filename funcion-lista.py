# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 19:08:43 2020

@author: CEC
"""

def createList(n):
    myList = []
    for i in range(n):
        myList.append(i)
    return myList

print(createList(8))