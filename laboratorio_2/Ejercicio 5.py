#!/usrbin/env python
# _*_ coding: utf-8 _*_
#Tarea 2 Ejercicio 5
#Ulises Bruno Lozano
#08/12/16
import matplotlib.pyplot as plt
import numpy as np
cx=input("Introduce la magnitud del lado de una figura geometrica: ")
def juegodelcaos2(x):
    x=cx
    y=np.linspace(0,x,100)
    figura=[]
    for i in y:
        figura.append(i**i+i**i)
    plt.plot(y,figura)
    plt.show()
salida=juegodelcaos2(cx)
