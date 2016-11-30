#Ejercicio 3 tarea 3
#Ulises Bruno Lozano
#29/11/16
a=input("Introduce un numero entero de 3 digitos: ")
def funcion(x):
    x=a
    c=str(x)
    if c[0]<c[1]<c[2]:
        d=c[0],c[1],c[2]
        print d
    if c[1]<c[0]<c[2]:
         e=c[1],c[0],c[2]
         print e
    if c[2]<c[1]<c[0]:
        f=c[2],c[1],c[0]
        print f
    if c[2]<c[0]<c[1]:
        g=c[2],c[0],c[1]
        print g
    if c[0]<c[2]<c[1]:
        h=c[0],c[2],c[1]
        print h
    if c[1]<c[2]<c[0]:
        j=c[1],c[2],c[0]
        print j

output=funcion(a)
