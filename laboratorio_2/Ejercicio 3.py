#Tarea 2 Ejercicio 3
#Ulises Bruno Lozano
#25/11/16
import matplotlib.pyplot as plt
cx=input("Introduce la magnitud del lado de un triangulo rectangulo: ")
def juegodelcaos(x):
    x=cx
    p0=[0,0]
    p1=[0,cx]
    p2=[cx/2,cx]
    triangulo=[[0,0],[0,cx],[cx/2,cx]]
    plt.plot(triangulo)
    plt.show()

salida=juegodelcaos(x)
print salida
