import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.arange(-10, 10, .5)
y = np.arange(-10, 10, .5)
x, y = np.meshgrid(x, y)
z = (np.sin(np.abs(x) - np.abs(y)))

ax.plot_trisurf(x.flatten(), y.flatten(), z.flatten(), color = 'red', edgecolor = 'k', linewidth = 0.5)
ax.set_title('$z = sin(|x| - |y|)$')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()