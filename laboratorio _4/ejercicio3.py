#!/usrbin/env python
# _*_ coding: utf-8 _*_
#Laboratorio 4 Ejercicio 3
#Ulises Bruno Lozano
#18/12/16
x=raw_input("Introduzca el nombre de un archivo:")
y=raw_input("Introduzca el nombre del archivo una vez editado:")
def ejercicio3(a,b):
    a=x
    b=y
    archivo=open(a,'r')
    edicion=0
    archivo2=open(b,'w')
    copy=archivo.readlines()
    for i in copy:
        edicion=edicion+1
        archivo2.write(str(edicion)+str(i)+" ")
        print edicion
        print i
output=ejercicio3(x,y)
