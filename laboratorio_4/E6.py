#Tarea 4 Ejercicio 6
#Ulises Bruno Lozano
#03/12/16
import matplotlib.pyplot as plt
import numpy as np
import math
teta=np.linspace(0,2*np.pi,100)
r=-250*np.sin(5*teta)*np.cos(4*teta)
yt=teta+np.sin(r/100)
x=320+r*np.cos(yt)
y=-240-r*np.sin(yt)
plt.plot(x,y,linewidth=3,color='black',label='(x,y)')
plt.fill_between(x,y,color='r')
plt.legend()
plt.title('')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axis('equal')
plt.axis('off')
plt.show()
plt.savefig('grafica6.png')
