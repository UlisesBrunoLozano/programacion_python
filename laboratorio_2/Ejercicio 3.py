#!/usrbin/env python
# _*_ coding: utf-8 _*_
#Tarea 2 Ejercicio 3
#Ulises Bruno Lozano
#25/11/16
import matplotlib.pyplot as plt
cx=input("Introduce la magnitud del lado de un triangulo rectangulo: ")
def juegodelcaos(x):
    x=cx
    triangulo=[[0,0],[0,x],[x/2,x],[0,0]]
    plt.plot(triangulo)
    plt.show()
salida=juegodelcaos(cx)
