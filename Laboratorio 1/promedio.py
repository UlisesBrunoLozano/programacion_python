#!/usrbin/env python
# _*_ coding: utf-8 _*_
#Ulises Bruno Lozano
#Promedio
#18/11/12
a=(input("Introduzca sus calificaciones separadas por coma: "))
def promedio(x):
    x=a
    y=[]
    suma=0.0
    for i in x:
        y.append(i)
        suma=suma+i
    print (suma/len(y))
output=promedio(a)
