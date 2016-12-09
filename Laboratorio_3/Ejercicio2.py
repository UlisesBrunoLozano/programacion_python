#!/usrbin/env python
# _*_ coding: utf-8 _*_
#Ejercicio 2 tarea 3
#Ulises Bruno lozano
#29/11/2016
a=input("A continuacion introduzca un numero de cuatro digitos: ")
def digitos(x):
    x=a
    b=str(x)
    suma=int(b[0])+int(b[1])+int(b[2])+int(b[3])
    print "La suma de los digitos es =",suma
output=digitos(a)
