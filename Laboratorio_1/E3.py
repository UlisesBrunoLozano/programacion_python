#!/usrbin/env python
# _*_ coding: utf-8 _*_entrada=input("Introduzca un entero positivo ")
#Ulises Bruno Lozano
#08/12/16
entrada3=input("Introduzca un radio: ")
def funcion3(x):
    x=entrada3
    pi=3.1416
    Area=pi*x*x
    Volumen=(3*pi*x*x*x)/4
    print "Area del circulo: ",+Area
    print "Volumen de la esfera: ",+Volumen
salida3=funcion3(entrada3)
