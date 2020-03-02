# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 19:20:24 2020

@author: CEC
"""

def isPrime(num):
    if num <2 :
        return False
    for x  in range(2, num):    
        if (num % x)== 0:
            #print("Es primo")
            return False
    return True

isPrime(7)
    

for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()
