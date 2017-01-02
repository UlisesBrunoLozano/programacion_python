#!/usrbin/env python
# _*_ coding: utf-8 _*_
#Laboratorio 4 Ejercicio 2
#Ulises Bruno Lozano
#18/12/16
a=raw_input("Introduzca una lista de archivos:").strip().split(',')
b=int(raw_input("Introduce las lineas que deseas unir: ").strip())
def laboratorio(x,y):
    x=a
    y=b
    for e in x:
        archivo=open((e),"r")
        for i in range(b):
            print archivo.readline()
output=laboratorio(a,b)
