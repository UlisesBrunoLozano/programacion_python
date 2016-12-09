#!/usrbin/env python
# _*_ coding: utf-8 _*_
#Tarea 4 Ejercicio 7
#Ulises Bruno Lozano
#03/12/16
import matplotlib.pyplot as plt
import numpy as np
import math
teta=np.linspace(0,2*np.pi,100)
r=105+100*np.sin(4.5*teta)
yt=teta-np.cos(10*teta)/10
x=320+r*np.cos(yt)
y=-240-r*np.sin(yt)
plt.plot(x,y,linewidth=3,color='red',label='(x,y)')
plt.fill_between(x,y,color='pink')
plt.legend()
plt.title('')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axis('equal')
plt.axis('off')
plt.show()
plt.savefig('grafica7.png')
