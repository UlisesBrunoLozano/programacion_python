#!/usrbin/env python
# _*_ coding: utf-8 _*_
#Ejercicio 1
#Ulises Bruno Lozano
#29/11/2016
import matplotlib.pyplot as plt
import math as m
import numpy as np
a=input("Introduce la latitud de tu punto inicial: ")
b=input("Introduce la longitud de tu punto inicial: ")
c=input("Introduce la latitud del punto final: ")
d=input("Introduce la longitud del punto final: ")
def distancia(t1,g1,t2,g2):
    Pi=3.1415
    t1=(a*Pi/180)
    g1=(b*Pi/180)
    t2=(c*Pi/180)
    g2=(d*Pi/180)
    sins=m.sin(t1)*m.sin(t2)+m.cos(t1)*m.cos(t2)*m.cos(g1-g2)
    arrow=6371.01*m.acos(sins)
    return arrow
    print arrow

output=distancia(a,b,c,d)
print output
