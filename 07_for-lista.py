# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:27:10 2020

@author: CEC
"""

devices=["R1","R2","R3","S1","S2"]
switches=[]
for item in devices:
    if "S" in item:
        switches.append(item)
print(switches)
