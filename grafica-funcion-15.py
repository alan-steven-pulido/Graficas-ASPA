import matplotlib.pyplot as plt
import numpy as np

theta = np.arange(0, 4*np.pi, 0.04)
r = 105 + (100*(np.sin(4.5*theta)))
lmda = theta - (np.cos(10 * theta)/10) 

x = 320 * r * np.cos(lmda)
y = -240 * -r * np.sin(lmda)

plt.plot(x, y, linewidth = 3, color = 'k')
plt.fill_between(x, y, color = 'blue')

plt.title('$x = 320rcos(lamda)$' + '   $y = -240-rsin(lamda)$')
plt.axis('equal')
plt.axis('off')

plt.show()