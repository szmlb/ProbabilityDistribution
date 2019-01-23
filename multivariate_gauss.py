import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# inputs
x, y = np.meshgrid(np.linspace(-4, 4, 100), np.linspace(-4, 4, 100))
pos = np.dstack((x,y))

# probability distribution
mean = np.array([0.0, 0.0])
cov  = np.array([[3.0, 0.0], [0.0, 3.0]])
z = scipy.stats.multivariate_normal(mean, cov).pdf(pos)

# plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(x, y, z, cmap=cm.gray)
fig.colorbar(surf)
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('pdf')
plt.show()
