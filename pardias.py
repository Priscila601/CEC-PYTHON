# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 20:47:58 2020

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
   


def daysInMonth(year, month):
    if year <1900 or month >=1 and month <=12:
        if isYearLeap(year):
            diasmes=[0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            diasmes=[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for x, y in enumerate(diasmes):
            if x == month:
                return y
                #print(y)
    else:
         return None
      
        
print(daysInMonth(2020,1))

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
