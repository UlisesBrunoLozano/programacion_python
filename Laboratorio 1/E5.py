#!/usrbin/env python
# _*_ coding: utf-8 _*_entrada=input("Introduzca un entero positivo ")
#Ulises Bruno Lozano
#08/12/16
a=input("Introduzca los segundos que viajo: ")
def funcion2(a):
    dias=a/(86400)
    b=a/float(86400)
    resto=abs(b)-abs(int(b))
    horas=resto*10**6/3600
    resto2=abs(resto/float(3600))-abs(int(resto/float(3600)))
    minutos=resto2*10**6/60
    segundos=abs(minutos/float(60))-abs(int(minutos/float(60)))
    print ("Su viaje duro", dias,"dias", horas,"horas", minutos,"minutos y",segundos,"segundos")
salida2=funcion2(a)
