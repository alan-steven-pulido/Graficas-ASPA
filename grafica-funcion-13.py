import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2*np.pi)
r = (2 - 2*np.sin(theta)) + np.sin(theta)*np.divide(np.sqrt(np.absolute(np.cos(theta))), (np.sin(theta) + 1.4))

x = r * np.cos(theta)
y = r * np.sin(theta)

plt.plot(x, y, linewidth = 3, color = 'k')
plt.fill_between(x, y, color='red')

plt.axis('equal')
plt.axis('off')

plt.show()