#!/usrbin/env python
# _*_ coding: utf-8 _*_
#Ejercicio 6 tarea 3
#Ulises Bruno Lozano
#29/11/16
a=input("Introduce tu edad: ")
def aperro(x):
    x=a
    ap=10.5
    if 0<x<2:
        print "Usted tiene",x*ap,"años perro."
    else:
        print "Usted tiene",x*4,"años perro."
output=aperro(a)
