#Tarea 2 Ejercicio 4
#Ulises Bruno Lozano
#25/11/16
import matplotlib.pyplot as plt
x=input("Ingrese los lados de un poligono regular: ")
for x in range(0,x):
    if x%2==0:
      p0=[0,0]
      p1=[x,0]
      p2=[x,x]
      p3=[0,0]
      n=[[p0],[p1],[p2],[p3]]
    print n
    plt.plot(n)
    plt.show()

salida=n(x)
print salida
