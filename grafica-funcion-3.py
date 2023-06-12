import matplotlib.pyplot as plt
import numpy as np

tpoints = np.linspace( -1, 5, 300)
def f(t):
    return (tpoints * np.exp(-2*tpoints))

plt.plot(tpoints, f(tpoints),'3', linewidth = 2, color = 'k', markersize = 10)
plt.title('f(t) = $t.exp^{(-0.1t)}$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')
plt.grid(True)
plt.show()