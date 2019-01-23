import numpy as np
import scipy.stats
from matplotlib import pyplot as plt

param = 0.5
#param = 4.0
#param = 1.0

# probability distribution
x = np.arange(scipy.stats.poisson.ppf(0.01, mu=param), scipy.stats.poisson.ppf(0.99, mu=param))
rv = scipy.stats.poisson(mu=param)
y = rv.pmf(x)

# plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(x, y)
ax.set_xlim([0, 12])
ax.set_title('$\lambda$=%.1f' % (param))
plt.show()
