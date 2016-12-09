#!/usrbin/env python
# _*_ coding: utf-8 _*_
#Ejercicio 3 tarea 3
#Ulises Bruno Lozano
#29/11/16
a=input("Introduce un numero entero de 3 digitos: ")
def funcion(x):
    x=a
    c=str(x)
    if c[0]<=c[1]<=c[2]:
        d=c[0],c[1],c[2]
        print d
    elif c[1]<=c[0]<=c[2]:
        e=c[1],c[0],c[2]
        print e
    elif c[2]<=c[1]<=c[0]:
        f=c[2],c[1],c[0]
        print f
    elif c[2]<c[0]<c[1]:
        g=c[2],c[0],c[1]
        print g
    elif c[0]<=c[2]<=c[1]:
        h=c[0],c[2],c[1]
        print h
    elif c[1]<=c[2]<=c[0]:
        j=c[1],c[2],c[0]
        print j
output=funcion(a)
