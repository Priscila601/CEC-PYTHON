# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 08:34:39 2020

@author: CEC
"""

def isYearLeap(year):
    if (year % 4 !=0):
        return False
    elif year % 100!= 0:
        return True
    elif (year % 400 !=0):
        return False
    else:
        return True

def daysInMonth(year,month):
	if year < 1900 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month-1]
	if month == 2 and isYearLeap(year):
		res = 29
	return res

def dayOfYear(year, month, day):
    if year<1800 or month <1 or month >12 or day<1 or day>31:
        return None
    cont=0    
    for d in range(1,month):
        m= daysInMonth(year,d)
        if m==None:
            return None
        cont+= m
    return cont+day       

print(dayOfYear(2019, 12,31 ))
