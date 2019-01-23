import numpy as np
import scipy.stats
from matplotlib import pyplot as plt

#param = [10, 0.5]
#param = [10, 0.2]
param = [20, 0.6]

# probability distribution
x = np.arange(scipy.stats.binom.ppf(0.01, n=param[0], p=param[1]), scipy.stats.binom.ppf(0.99, n=param[0], p=param[1]))
rv = scipy.stats.binom(n=param[0], p=param[1])
y = rv.pmf(x)

# plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(x, y)
ax.set_xlim([0, 20])
ax.set_title('M=%d, $\mu$=%.1f' % (param[0], param[1]))
plt.show()
