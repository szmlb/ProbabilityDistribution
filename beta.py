import numpy as np
import scipy.stats
from matplotlib import pyplot as plt

x = np.linspace(0, 1, 1000)
plt.xlim(0, 1)
plt.ylim(0, 8)
params = [[0.5, 0.5], [0.6, 0.8], [1.0, 1.0], [10.0, 40.0], [10.0, 5.0]]
for param in params:
    rv = scipy.stats.beta(param[0], param[1])
    y = rv.pdf(x)
    plt.plot(x, y, '-', lw=2, label="a="+str(param[0])+", b="+str(param[1]))
plt.legend()
plt.show()
