import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

"""
# inputs
x, y = np.meshgrid(np.linspace(0, 1, 100), np.linspace(0, 1, 100))
pos = np.dstack((x,y))

# probability distribution
alpha = np.array([0.4, 5, 15])  # specify concentration parameters
rv = scipy.stats.dirichlet(alpha)
z = rv.pdf(pos)
"""


# triangle mesh grid (0,0)-(1,0)-(0,1)
xx = np.array([[0.01*a*0.01*(100-b) for a in range(1, 100)] for b in range(1, 100)])
yy = np.array([[0.01*b] * 99 for b in range(1, 100)])

# Dirichlet PDF on mesh grid ((0,0)->(0,0,1), (1,0)->(1,0,0), (0,1)->(0,1,0))
alpha = np.array([0.4, 5, 15])  # specify concentration parameters
di = scipy.stats.dirichlet(alpha)
Z = di.pdf([xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# transform isosceles right triangle mesh into equilateral triangle
xx2 = np.array([x + (0.5 - np.average(x)) for x in xx])
yy2 = yy * np.sqrt(3) / 2

# 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(xx2, yy2, Z, cmap=cm.gray)
fig.colorbar(surf)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.show()
