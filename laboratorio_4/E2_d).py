#Tarea 4 Ejercicio 2 d)
#Ulises Bruno Lozano
#03/12/16
import matplotlib.pyplot as plt
import numpy as np
import math
t=np.linspace(0,2*np.pi,100)
e=1+2*np.sin(t)
f=1+2*np.sin(t)
X=e*np.cos(t)
Y=f*np.sin(t)
plt.plot(t,X,linewidth=4,color='black',label='x(t)')
plt.plot(t,Y,linewidth=5,color='brown',label='y(t)')
plt.legend('XY')
plt.title('')
plt.xlabel('t')
plt.ylabel('X(t)&Y(t)')
plt.grid(True)
plt.show()
plt.savefig('grafica2d.png')
