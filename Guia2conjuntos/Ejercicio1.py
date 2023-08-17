# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 16:21:28 2023

@author: usuario
"""

from sympy import FiniteSet

A = FiniteSet("a", "b", "c", "d", "e")
B = FiniteSet("b", "d", "e")

#Union de 2 conjuntos
UnionConjuntos = A.union(B)
print("Union de conjuntos con Finiset: ", UnionConjuntos)
 
#Interseccion de 2 conjuntos
UnionConjuntos = A.intersect(B)
print("Interseccion de conjuntos con FiniSet: ", UnionConjuntos)

#Diferencia de 2 conjuntos
Diferencia = B-A
print("Diferencia de conjuntos con FiniteSet", Diferencia)    

#Conjunto potencia de A
Potencia = A.powerset();
print("Conjunto potencia de A es ", Potencia)
#Cardinalidad
print("La cardinalidad del conjunto potencia es: ", len(Potencia));