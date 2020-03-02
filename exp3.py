# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 12:51:53 2020

@author: CEC
"""

try:
    x = int(input("Enter a number:"))
    y= 1/ x
    print(y)
    
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")

except ValueError:
    print("You must enter a integer value")

except:
    print("Oh dear, something went wrong")
    
print("THE END")