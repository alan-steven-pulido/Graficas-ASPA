import matplotlib.pyplot as plt
import numpy as np

xpoints = np.linspace( 0, 2, 100)
def f(x):
    return ((xpoints) * (np.exp(-3*xpoints)))

def g(x):
    return ((np.exp(-3*xpoints))*(1-(3*xpoints)))

plt.plot(xpoints, f(xpoints),'o:c', markersize = 10, label = 'f(x)')
plt.plot(xpoints, g(xpoints),'3', color = 'm', markersize = 10, label = 'g(x)')
plt.title('$f(x) = xe^{-3x}$'+'   $g(x) = e^{-3x}(1-3x)$')
plt.legend( )
plt.ylabel('Eje y')
plt.xlabel('Eje x')
plt.grid(True)
plt.show()