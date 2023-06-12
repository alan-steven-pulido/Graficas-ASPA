import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.arange(-2, 2, 0.2)
y = np.arange(-2, 2, 0.2)
x, y = np.meshgrid(x, y)
z = x**2 - y**2

ax.plot_wireframe(x, y, z, color = 'k')
ax.set_title('$z = x^2 - y^2$')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()