# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 19:57:41 2020

@author: CEC
"""

#	1 milla americana = 1609.344 metros;
#	1 galón americano = 3.785411784 litros.


def l100kmtompg(litres):    
    #return (int(liters)*100000/(3.785411784*1609.344 ))
    gallons=litres/3.785411784
    miles= (100*1000)/1609.344
    
    return gallons/miles

def mpgtol100km(miles):
    #return (int(miles)*1609.344)
    litres =3.785411784
    
    return litres/km100

print(l100kmtompg(3.9))
