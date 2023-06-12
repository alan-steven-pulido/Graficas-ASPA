import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos

tpoints = np.linspace( 0, 2*np.pi, 100)
def x(t):
    return ((1 + (2 * sin(2*tpoints))) * cos(tpoints))

def y(t):
    return ((1 + (2 * sin(tpoints))) * sin(tpoints))

plt.plot(tpoints, x(tpoints),'o:c', markersize = 10, label = 'x(t)')
plt.plot(tpoints, y(tpoints),'o--m', markersize = 10, label = 'y(t)')
plt.title('$x(t) = (1 + 2sin(t))cos(t)$'+'   $   y(t) = (1 + 2sin(t))sin(t)$')
plt.legend( )
plt.ylabel('Eje y')
plt.xlabel('Eje x')
plt.grid(True)
plt.show()