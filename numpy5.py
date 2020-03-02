# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 11:40:52 2020

@author: CEC
"""
import numpy as np

#matriz de unos
unos=np.ones((3,4))
print(unos)

#matriz de ceros
ceros=np.zeros((3,4))
print(ceros)

#crear matriz valores aleatorios
aleatorios=np.random.random((2,2))
print(aleatorios)

#crear matriz vacia
vacia=np.empty((3,4))
print(vacia)


#matriz con un solo valor
full=np.full((2,2),47)
print(full)

#crear matriz con valores espaciados uniformemente
espacio1=np.arange(0,30+1,5)
print(espacio1)

#crear matriz con valores entre 0 y 2
espacio2 = np.linspace(0,2,10)
print(espacio2)

#crear matriz  identidad
identidad1=np.eye(4,4)
print(identidad1)
identidad2=np.eye(4)
print(identidad2)

#conocer las dimensiones de una matriz
a = np.array([(1,2,3),(4,5,6)])
print(a.ndim)

#conocer el tipo de datos
a =np.array([(1,2,3)])
print()
# conocer el tamaño y forma de matriz


#cambio de forma de una matriz
a = np.array([(8,9,10),(11,12,13)])
print(a)
print("\n"*2)
a =a.reshape(3,2)
print(a)


#devolver valor almacenado en posicion de matriz

a = np.array([(1,2,3,4),(3,4,5,6)])
print(a)
print("\n"*1)
print(a[1,2])


#obtener valores ubicados en la fila especificada
a = np.array([(1,2,3,4),(3,4,5,6)])
print(a[0:,1])

#encontrar valor mi
a = np.array([2,4,8])
print(a.min())
print(a.max())
print(a.sum())



#
a=np.array([(1,2,3),(3,4,5)])
print("\n"*2)
print(np.sqrt(a))

#operaciones con matrices
x=np.array([(1,2,3),(3,4,5)])
y=np.array([(1,2,3),(3,4,5)])

print(x+y)
print("\n")
print(x-y)
print("\n")
print(x*y)
print("\n")
print(x/y)


























