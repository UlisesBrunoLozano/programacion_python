#!/usrbin/env python
# _*_ coding: utf-8 _*_
#Tarea 2 Ejercicio 2
#Ulises Bruno Lozano
#25/11/16
entrada=input("Ingrese la distancia recorrida en km: ")
def tarifa(x):
    distancia=[x]
    banderazo=8.74
    km=1.84*4
    pagar=0
    for x in distancia:
        pagar=pagar+banderazo+(x*km)
        print "Usted tendra que pagar",pagar,"pesos."
salida=tarifa(entrada)
