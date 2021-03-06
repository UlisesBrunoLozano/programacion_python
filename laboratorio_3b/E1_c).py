#!/usrbin/env python
# _*_ coding: utf-8 _*_
#Tarea 4 Ejercicio 1 c)
#Ulises Bruno Lozano
#02/12/16
import matplotlib.pyplot as plt
import numpy as np
import math
x=np.linspace(-1,5,93)
t=x
y=t*math.e**(-2*t)
plt.plot(x,y,linewidth=7,color='b',label='Inciso c')
plt.legend()
plt.title('')
plt.xlabel('t')
plt.ylabel('f(t)=te**-2*t')
plt.grid(True)
plt.show()
plt.savefig('grafica1c.png')
