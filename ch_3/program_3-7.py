"""Listing 3.7, page 81"""

import numpy as np
import math
import matplotlib.pyplot as plt

n_meas = 50000
n_pert = 20

meas = np.random.rand(n_meas, n_pert)
meas = np.sum(meas, axis=1)

mean = np.mean(meas)
sigma = np.std(meas, ddof=1)

def f(x):
    a = 1 / (math.sqrt(2 * math.pi) * sigma)
    return a * np.exp(-(x - mean)**2 / (2 * sigma**2))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Measurement result')
ax.set_ylabel('Probability density')
ax.grid()

p, bins, _ = ax.hist(meas, bins=51, density=True)
ax.plot(bins, f(bins))
plt.show()
