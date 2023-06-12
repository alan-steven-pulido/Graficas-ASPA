import matplotlib.pyplot as plt
import numpy as np
from numpy import sin

tpoints = np.linspace( 0, 24, 250)
def h(t):
    return (sin(2*tpoints)* np.exp(-0.1*tpoints))

plt.plot(tpoints, h(tpoints),'*', color = 'b', markersize = 10)
plt.title('h(t) = $sin(2t)exp^{-0.1t}$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')
plt.grid(True)
plt.show()