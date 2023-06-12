import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.arange(-1, 1, .1)
y = np.arange(-1, 1, .1)
x, y = np.meshgrid(x, y)
z = (np.cos(np.abs(x) + np.abs(y)))

ax.plot_trisurf(x.flatten(), y.flatten(), z.flatten(), color = 'red')
ax.set_title('$z = cos(|x| + |y|)$')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()