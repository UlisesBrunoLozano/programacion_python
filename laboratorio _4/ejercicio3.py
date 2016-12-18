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
    lineas=len(archivo.readlines())
    edicion=[]
    copy=archivo.readlines()
    for i in range(0,lineas+1):
        edicion.append(i)
    archieditado=open(b,'w')
    for i in copy:
        archieditado.write(str(i))
    for e in edicion:
        archieditado.write(str(e)+"\n")
output=ejercicio3(x,y)
