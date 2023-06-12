import matplotlib.pyplot as plt
import numpy as np
from numpy import sin

tpoints = np.linspace( 0, 2*np.pi, 170)
def x(t):
    return (sin(3*tpoints))

def y(t):
    return (sin(4*tpoints))

plt.plot(x(tpoints), y(tpoints),'o--g', markersize = 7, mec = 'k', mfc = 'r')
plt.title('$x = sin(3t)$'+'   $y = sin(4t)$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')
plt.grid(True)
plt.show()