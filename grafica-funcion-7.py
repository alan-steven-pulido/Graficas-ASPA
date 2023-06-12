import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos

tpoints = np.linspace( 0, 4*np.pi, 100)
def f(t):
    return ((sin(3*tpoints)*(cos(2*tpoints))))

def g(t):
    return ((0.5)*(cos(tpoints)*(5/2)+(cos(5*tpoints))))

plt.plot(tpoints, f(tpoints),'o--c', markersize = 10, label = 'f(t)')
plt.plot(tpoints, g(tpoints),'o--m', markersize = 10, label = 'g(t)')
plt.title('$f(t) = sin(3t)cos(2t)$'+'   $   g(t) = 1/2 cos(t)+5/2 cos(5t)$')
plt.legend( )
plt.ylabel('Eje y')
plt.xlabel('Eje x')
plt.grid(True)
plt.show()