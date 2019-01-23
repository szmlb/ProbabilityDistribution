import numpy as np
import scipy.stats
from matplotlib import pyplot as plt

param = 0.2
x = np.linspace(0, 1, 2)
rv = scipy.stats.bernoulli(p=param)
y = rv.pmf(x)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.bar(x, y)
ax.set_ylim(0, 1)
plt.show()
