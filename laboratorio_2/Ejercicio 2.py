#Tarea 2 Ejercicio 2
#Ulises Bruno Lozano
#25/11/16
entrada=input("Ingrese la distancia recorrida: ")
def tarifa(x):
    distancia=[x]
    banderazo=8.74
    km=1.84*4
    pagar=0
    for x in distancia:
        pagar=pagar+banderazo+(x*km)
        print pagar

salida=tarifa(entrada)
print salida 
