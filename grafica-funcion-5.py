import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos

xpoints = np.linspace( 0, 4*np.pi, 200)
def s(x):
    return ((cos(2 * xpoints)) + (sin(3 * xpoints)))

def v(x):
    return ((-sin(2 * xpoints)) + (3*cos(3 * xpoints)))

plt.plot(xpoints, s(xpoints),'*', color = 'b', markersize = 10, label = 's(x)')
plt.plot(xpoints, v(xpoints),'3', color = 'r', markersize = 10, label = 'v(x)')
plt.title('s(x) = cos(2x)+sin(3x)'+'   v(x) = -2sin(2x)+3cos(3x)')
plt.legend( )
plt.ylabel('Eje y')
plt.xlabel('Eje x')
plt.grid(True)
plt.show()