import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.arange(-5, 5, .1)
y = np.arange(-5, 5, .1)
x, y = np.meshgrid(x, y)
z = (np.abs(np.cos(x) + np.cos(y)))**0.5

ax.plot_surface(x, y, z, color = 'b', linewidth = 15 )# Si pongoi el linewidth = 0 el ancho de la superficie se hace mas delgada, pero se sigue viendo igual.
ax.set_title('$z = |cos(x) + cos(y)|^{1/2}$')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()