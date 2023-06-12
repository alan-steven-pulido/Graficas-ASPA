import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos

tpoints = np.linspace( 0, 2*np.pi, 100)
def x(t):
    return (cos(tpoints)**3)

def y(t):
    return (sin(tpoints)**3)

plt.plot(x(tpoints), y(tpoints),'o-c', markersize = 7, mec = 'k', mfc = 'm')
plt.title('$x = cos^3(t)$'+'   $y = sin^3(t)$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')
plt.grid(True)
plt.show()