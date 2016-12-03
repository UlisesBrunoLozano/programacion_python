#Tarea 2 Ejercicio 1
#Ulises Bruno Lozano
#25/11/16
import math as m
ladoa=input("Ingresa el lado a de un triangulo rectangulo: ")
ladob=input("Ingresa el lado b de un triangulo rectangulo: ")
def hipotenusa(a,b):
    a=ladoa
    b=ladob
    h=m.sqrt(a*a+b*b)
    print h
salida=hipotenusa(ladoa,ladob)
print salida
