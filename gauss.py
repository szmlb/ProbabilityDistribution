import numpy as np
import scipy.stats
from matplotlib import pyplot as plt

x = np.linspace(-10, 10, 1000)
plt.xlim(-10, 10)
plt.ylim(0, 1.4)
params = [[0.0, 1.0], [2.0, 2.0], [-6.0, 0.3]]
for param in params:
    rv = scipy.stats.norm(loc=param[0], scale=param[1])
    y = rv.pdf(x)
    plt.plot(x, y, '-', lw=2, label="$\mu$="+str(param[0])+", $\sigma$="+str(param[1]))
plt.legend()
plt.show()
