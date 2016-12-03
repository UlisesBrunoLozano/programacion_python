entrada=input("Introduzca un entero positivo ")
def funcion1(x):
    suma=0
    listax=[x for x in range(0,x+1)]
    for x in listax:
        suma=x+suma
    return suma
salida=funcion1(entrada)
print salida
