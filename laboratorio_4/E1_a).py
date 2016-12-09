#!/usrbin/env python
# _*_ coding: utf-8 _*_
#Tarea 4 Ejercicio 1 a)
#Ulises Bruno Lozano
#02/12/16
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-6,2,93)
y=-x**2-4*x+5
plt.plot(x,y,linewidth=3,color='r',label='Inciso a)')
plt.legend()
plt.title('')
plt.xlabel('x')
plt.ylabel('f(x)=-x^2-4x+5')
plt.grid(True)
plt.show()
plt.savefig('grafica1a.png')
