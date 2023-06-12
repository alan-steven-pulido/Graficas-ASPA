import matplotlib.pyplot as plt
import numpy as np

xpoints = np.linspace( -6, 2, 200)
def f(x):
    return (5 - (4*xpoints)- (xpoints**2))

plt.plot(xpoints, f(xpoints),'o:g', markersize = 10)
plt.ylabel('Eje y')
plt.xlabel('Eje x')
plt.grid(True)
plt.show()