#!/usrbin/env python
# _*_ coding: utf-8 _*_entrada=input("Introduzca un entero positivo ")
#Ulises Bruno Lozano
import math
a=input("Peso(kg): ")
h=input("Altura(cm): ")
def masacorporal(peso, altura):
    peso=a
    alturacm=h
    alturam=h/float(100)
    IMC=peso/float(alturam)**2
    if IMC<16:
        print "Delgadez severa"
    elif IMC>16 and IMC<19.99:
        print "Delgadez moderada"
    elif IMC>17 and IMC<18.49:
        print "Delgadez leve"
    elif IMC>18.5 and IMC<24.99:
        print "Normal"
    elif IMC>25 and IMC<30:
        print "Sobrepeso"
    elif IMC>30 and IMC<40:
        print "Obesidad"
    elif IMC>40:
        print "Obesidad morbida"
output=masacorporal(a,h)
