import matplotlib.pyplot as plt
import numpy as np

theta = np.arange(0, 2*np.pi, 0.015)
r = 250*(np.sin(5*theta)) * (np.cos(4*theta)) 
lmda = theta + np.sin(r/100)

x = 320 * r * np.cos(lmda)
y = -240 * -r * np.sin(lmda)

plt.plot(x, y, linewidth = 3, color = 'k')
plt.fill_between(x, y, color='green')

plt.axis('equal')
plt.axis('off')

plt.show()