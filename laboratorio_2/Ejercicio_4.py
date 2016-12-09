#!/usrbin/env python
# _*_ coding: utf-8 _*_
#Tarea 2 Ejercicio 4
#Ulises Bruno Lozano
#25/11/16
import matplotlib.pyplot as plt
import numpy as np
a=input("Ingrese los lados de un poligono regular: ")
x=np.linspace(0,1,100)
lista=[]
for i in range(a):
    x1=[0,i]
    y1=[i,0]
    lista.append(x1+y1)
print lista
