# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 19:10:35 2020

@author: CEC
"""

lista = [1,2,3,4,5]
ix=0
doit=True

while doit:
    try:
        print(lista[ix])
        ix +=1
    except IndexError:
        doit=False
        
print("listo")