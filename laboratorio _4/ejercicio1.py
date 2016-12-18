#!/usrbin/env python
# _*_ coding: utf-8 _*_
#Laboratorio 4 Ejercicio 1
#Ulises Bruno Lozano
#18/12/16
a=raw_input("Introduce el nombre de un archivo: ")
b=input("Introduzca el nùmero de lineas que desea leer: ")
def laboratorio(x,y):
    x=a
    y=b
    archivo=open(x,"r")
    for i in range(b):
        print archivo.readline()

output=laboratorio(a,b)
