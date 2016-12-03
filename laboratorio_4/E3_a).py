#Tarea 4 Ejercicio 3 a)
#Ulises Bruno Lozano
#03/12/16
import matplotlib.pyplot as plt
import numpy as np
import math
t=np.linspace(0,2*np.pi,100)
x=np.cos(t)*np.cos(t)*np.cos(t)
y=np.sin(t)*np.sin(t)*np.sin(t)
plt.plot(t,x,linewidth=3,color='b',label='t(x)')
plt.plot(t,y,linewidth=2,color='r',label='t(y)')
plt.legend('xy')
plt.title('')
plt.xlabel('t')
plt.ylabel('X(t)&Y(t)')
plt.grid(True)
plt.show()
plt.savefig('grafica3a.png')
