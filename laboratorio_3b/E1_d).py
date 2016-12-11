#!/usrbin/env python
# _*_ coding: utf-8 _*_
#Tarea 4 Ejercicio 1 d)
#Ulises Bruno Lozano
#02/12/16
import matplotlib.pyplot as plt
import numpy as np
import math
x=np.linspace(0,24,93)
m=np.sin(2*x)
n=-0.1*x
y=m*math.e**n
plt.plot(x,y,linewidth=1,color='y',label='Inciso d')
plt.legend()
plt.title('')
plt.xlabel('t')
plt.ylabel('h(t)=e^(-0.1*t)sen(2t)')
plt.grid(True)
plt.show()
plt.savefig('grafica1d.png')
