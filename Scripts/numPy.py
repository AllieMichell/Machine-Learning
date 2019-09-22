#!/usr/bin/python

import sys
import time
import numpy as np

print('MATRIZ UNIDIMENCIONAL Y BIDIMENCIONAL')
a=np.array([1,2,3])
print('1D array:')
print(a)
print()
b=np.array([(1,2,3),(4,5,6)])
print('2D array:')
print(b)

print('-------------')
print('LISTA DE MIL NUMEROS Y CALCULAMOS LA MEMORIA ASIGNADA A ESTA')
s = range(1000)
print('Resultado lista de Python:')
print(sys.getsizeof(5)*len(s))
print()
d = np.arange(1000)
print('Resutado NumPy array:')
print(d.size*d.itemsize)

print('-------------')
print('MODULO PARA EVALUAR LA RAPIDEZ EN LA QUE SE EJECUTAN ESTAS INSTRUCCIONES')
SiZE = 1000000
L1 = range(SiZE)
L2 = range(SiZE)
A1 = np.arange(SiZE)
A2 = np.arange(SiZE)

start = time.time()
result = [(x,y) for x,y in zip(L1, L2)]
print('Resultado lista de Python:')
print((time.time()-start)*1000)
print()
start = time.time()
result = A1 + A2
print('Resultado NumPy array:')
print((time.time()-start)*1000)

print('-------------')
print('CREAR UNA MATRIZ DE UNOS --> 3 FILAS Y 4 COLUMNAS ')
unos = np.ones((3,4))
print(unos)

print('CREAR UNA MATRIZ DE CEROS --> 3 FILAS Y 4 COLUMNAS ')
ceros = np.zeros((3,4))
print(ceros)

print('CREAR UNA MATRIZ DE NUMEROS ALEATORIOS --> 3 FILAS Y 4 COLUMNAS ')
aleatorios = np.random.random((3,4))
print(aleatorios)

print('CREAR UNA MATRIZ VACIA --> 3 FILAS Y 4 COLUMNAS ')
vacia = np.empty((3,4))
print(vacia)

print('CREAR UNA MATRIZ DE UN SOLO VALOR --> 3 FILAS Y 4 COLUMNAS ')
full = np.full((3,4),5)
print(full)

print('CREAR UNA MATRIZ CON VALORES ESPACIADOS UNIFORMEMENTE')
"""
Realiza una matriz de los números que se encuentran entre el cero y 30
haciendo saltos de 5 en 5
"""
espacio1 = np.arange(0,30,5) 
print(espacio1)
"""
Realiza una matriz de los de 5 valores con los números que se encuentran 
entre el 0 y 2
"""
espacio2 = np.linspace(0,2,5) #
print(espacio2)

print('CREAR UNA MATRIZ ENTIDAD')
identidad1 = np.eye(4,4)
print(identidad1)
identidad2 = np.identity(4)
print(identidad2)

print('CONOCER LAS DIMENCIONES DE UNA MATRIZ')
a = np.array([(1,2,3),(4,5,6)])
print(a.ndim)
print('CONOCER EL TIPO DE LOS DATOS')
print(a.dtype)
print('CONOCER EL TAMAÑO DE LA MATRIZ')
print(a.size)
print('CONOCER EL FORMA DE LA MATRIZ')
print(a.shape)

print('CAMBIO DE FORMA DE UNA MATRIZ')
print(a)
b = a.reshape(3,2)
print(b)

"""
Operaciones matemáticas 
"""
print('ENCONTRAR EL MINIMO, MAXIMO Y SUMA')
c = np.array([9,8,7,6,5,4,3,2,1])
print(c.min())
print(c.max())
print(c.sum())
print('CALCULAR LA RAÍZ CUADRADA Y DESVIACIÓN ESTÁNDAR')
d = np.array([(9,8,7,6,5), (4,3,2,1,0)])
print(np.sqrt(d))
print(np.std(d))
print('CALCULAR LA SUMA, RESTA, MULTIPLICACIÓN Y DIVISIÓN DE DOS MATRICES')
x = np.array([(1,3,5,7,9),(2,4,6,8,10)])
y = np.array([(10,9,8,7,6), (5,4,3,2,1)])
print(x+y)
print(x-y)
print(x*y)
print(x/y)