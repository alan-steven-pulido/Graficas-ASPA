import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.arange(-1, 1, 0.1)
y = np.arange(-1, 1, 0.1)
x, y = np.meshgrid(x, y)
z = (np.cos(np.abs(x) + np.abs(y)))*(np.abs(x) + np.abs(y))

ax.plot_wireframe(x, y, z, color = 'k')
ax.set_title('$z = cos(|x| + |y|)*(|x| + |y|)$')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()