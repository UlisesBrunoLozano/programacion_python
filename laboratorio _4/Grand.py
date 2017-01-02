#!/usrbin/env python
# _*_ coding: utf-8 _*_
#Laboratorio 4
#Ulises Bruno Lozano
#01/01/17
import csv
print "Saludos. Esta es una Tabla periodica interactiva. A continuacion se explica como funciona:"
print "I. Introduce alguna caracteristica del elemento cuyos datos deseas mostrar."
print "Por ejemplo:"
print "     12 mostrara <<Mg Magnesium 24.3050(6) [Ne]3s2>>, que se trata del Magnesio"
print "     de simbolo Mg, peso atomico de 24.3050 y con una configuracion 3s2 \n \n"
print "Asi mismo, si introduces Ununtrium o su simbolo, Uut, obtendras: "
print "    <<113 Uut Ununtrium	[284]	[Rn].5f14.6d10.7s2.7p1 \n \n \n"
a=raw_input("Introduce alguna caracteristica del elemento que buscas: ")
def laboratorio4(x):
    x=a
    with open('ptable.csv') as csvarchivo:
        entrada = csv.reader(csvarchivo)
        mod=[]
        for reg in entrada:
            mod.append(reg)
        for i in range(118):
            if x in mod[i]:
                print mod[i]
salida=laboratorio4(a)
