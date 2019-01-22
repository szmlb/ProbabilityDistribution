import numpy as np
import scipy.stats
from matplotlib import pyplot as plt

x = np.linspace(0, 10, 1000)
plt.xlim(0, 10)
plt.ylim(0, 1.1)
params = [[1.0, 1.0], [2.0, 2.0], [2.0, 0.5]]
for param in params:
    rv = scipy.stats.gamma(param[0], scale=1./param[1])
    y = rv.pdf(x)
    plt.plot(x, y, '-', lw=2, label="a="+str(param[0])+", b="+str(param[1]))
plt.legend()
plt.show()
