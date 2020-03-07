# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 09:19:12 2020

@author: CEC
"""

class Employee:
    'Common base class for all employees'
    empCount = 0
    
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount +=1
        
    def displayCount(self):
        print("Total Employee %d"%Employee.empCount)
        
    def displayEmployee(self):
        print("Name: ", self.name, ", Salary: ", self.salary )
        

emp1= Employee("Zara",2000)
emp2= Employee("Manni",5000)
emp3= Employee("Carla",3000)
emp4= Employee("Pablo",5000)

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
emp4.displayEmployee()

print("Total Employee %d" % Employee.empCount)

emp1.displayCount()