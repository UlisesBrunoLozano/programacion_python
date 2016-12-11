#!/usrbin/env python
# _*_ coding: utf-8 _*_
#Tarea 4 Ejercicio 3 c)
#Ulises Bruno Lozano
#03/12/16
import matplotlib.pyplot as plt
import numpy as np
import math
t=np.linspace(0,2*np.pi,100)
x=np.sin(3*t)
y=np.sin(4*t)
ax=plt.subplot(111, projection='polar')
plt.plot(t,x,linewidth=6,color='r',label='t(x)')
plt.plot(t,y,linewidth=3,color='y',label='t(y)')
plt.legend('xy')
plt.title('')
plt.xlabel('t')
plt.ylabel('t(x)&t(y)')
plt.grid(True)
plt.show()
plt.savefig('grafica3c.png')
