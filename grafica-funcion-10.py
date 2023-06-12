import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos

tpoints = np.linspace( -2*np.pi, 2*np.pi, 150)
def x(t):
    return (tpoints + 2*(sin(2*tpoints)))

def y(t):
    return (tpoints + 2*(cos(5*tpoints)))

plt.plot(x(tpoints), y(tpoints),'o--k', markersize = 7, mec = 'r', mfc = 'k')
plt.title('$x = t + 2sin(2t)$'+'   $y = t + 2cos(5t)$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')
plt.grid(True)
plt.show()