import matplotlib.pyplot as plt
import numpy as np

xpoints = np.linspace( -1, 5, 100)
def f(x):
    return ((2 * xpoints ** 2)-(8 * xpoints)-11)

plt.plot(xpoints, f(xpoints),'o:r', markersize = 10)
plt.ylabel('Eje y')
plt.xlabel('Eje x')
plt.grid(True)
plt.show()