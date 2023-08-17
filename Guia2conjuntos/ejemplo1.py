# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

A = {1, 4, 7, 9, 11}
"""
print(A)

#creando un conjunto a partir de una lista:
Lista = ["Toyota", "Mitsubishi", "Kia", "Fiat"]
#mostrando el contenido de la lista
print("La lista creada: ", Lista);
Conjunto = set(Lista);
print("El conjunto creado: ", Conjunto);
"""

#crea Lista con elementos repetidos                -01-
Lista2 = [13, 5, 5, 15, 7, 9, 9, 21, 5];
#crea conjunto con elementos de Lista2
OtroConjunto=set(Lista2);
print("Conjunto creado de la Lista 2 es ", OtroConjunto)

#                                                 -02-
Vacio = set();
print("Cardinalidad de conjunto vacio = ", len(Vacio));
print("Cardinalidad del 2do conjunto: ", len(OtroConjunto));

#Comprobando membresia, es decir, si un elemento pertenece a un conjunto -03-
if 9 in OtroConjunto: 
    print(9, "Esta dentro del 2do subconjunto");
    
#Comprobando la igualdad de conjuntos:                             -04-
    
B = [6, 9, 8, 3, 7]
B = set(B);
C = {8, 6, 13, 7, 9}
if C == B:
    print("conjuntos son iguales")
else:
    print("Conjuntos son distintos")

