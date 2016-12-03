#Tarea 4 Ejercicio 5 c)
#Ulises Bruno Lozano
#03/12/16
import matplotlib.pyplot as plt
import numpy as np
import math
teta=np.linspace(0,2*np.pi,100)
m=(abs(np.cos(teta)))**0.5
n=np.sin(teta)+1.4
r=2-2*np.sin(teta)+np.sin(teta)*m/n
x=r*np.cos(teta)
y=r*np.sin(teta)
plt.plot(x,y,linewidth=3,color='r',label='(x,y)')
plt.fill_between(x,y,color='red')
plt.legend()
plt.title('Te amo')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axis('equal')
plt.axis('off')
plt.show()
plt.savefig('grafica5c.png')
