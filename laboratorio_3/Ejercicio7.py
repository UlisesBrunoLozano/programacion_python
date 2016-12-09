#!/usrbin/env python
# _*_ coding: utf-8 _*_
#Ejercicio 7 tarea 3
#Ulises Bruno Lozano
#08/12/16
a=raw_input("Introduce tu nombre para jugar: ")
def thenamegame(x):
    z,b,c=a[0],a[1:],'bfm'
    if b[0] in c:b=b[1:]
    d="X,X,bo-@\nBanana-fana fo-@\nFee-fi-mo-@\nX!".replace('X',z)
    for y in c:d=d.replace('@',y+b,1)
    print d
output=thenamegame(a)
