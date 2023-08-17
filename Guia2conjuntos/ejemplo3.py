# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 16:05:34 2023

@author: usuario
"""

#Utilizando FiniSet de Python
from sympy import FiniteSet
C = FiniteSet(1,2,3)
print("utilizando FiniteSet: ", C)

#Generando al conjunto potencia
#Solo se puede hacer con FiniteSet
Potencia = C.powerset();
print("Conjunto potencia de C es ", Potencia)


#Cardinalidad
print("La cardinalidad del conjunto potencia es: ", len(C.powerset()))

#Igualdad
A = FiniteSet("x","w","m")
B = FiniteSet("x", "c", "t")

print("Conjuntos son A: ", A, " y B: ", B)

if A == B:
    print("Ambos conjuntos son iguales")
else: 
    print("Ambos conjuntos son distintos")
    
#Union de 2 conjuntos
UnionConjuntos = A.union(B)
print("Union de conjuntos con Finiset: ", UnionConjuntos)
 
#Interseccion de 2 conjuntos
UnionConjuntos = A.intersect(B)
print("Interseccion de conjuntos con FiniSet: ", UnionConjuntos)

#Diferencia de 2 conjuntos
Diferencia = A-B
print("Diferencia de conjuntos con FiniteSet", Diferencia)    