# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:27:45 2020

@author: CEC
"""

def reciproco(n):
    try:
        1/n
    except  ZeroDivisionError:
        print("Division fallida")
        return None
    else:
        print("Todo salió ien")
    finally:
        print("Es el momento de decir adios")
        return n
    

print(reciproco(2))

print(reciproco(0))