import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.arange(-2, 2, 0.2)
y = np.arange(-2, 2, 0.2)
x, y = np.meshgrid(x, y)
z = x**2 - y**2

ax.plot_surface(x, y, z, color = 'c', linewidth = 0 )# Si pongoi el linewidth = 0 el ancho de la superficie se hace mas delgada, pero se sigue viendo igual.
ax.set_title('$z = x^2 - y^2$')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
