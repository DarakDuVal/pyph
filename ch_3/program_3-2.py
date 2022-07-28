"""Listing 3.2, page 74"""

import numpy as np
import math
import matplotlib.pyplot as plt

def f(x, sigma):
    a = 1 / (math.sqrt(2 * math.pi) * sigma)
    return a * np.exp(-x**2 / (2 * sigma**2))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('x - <x>')
ax.set_ylabel('f(x)')
ax.grid()

x = np.linspace(-3, 3, 1000)
for sigma in [0.2, 0.5, 1.0, 2.0]:
    ax.plot(x, f(x, sigma), label=f'$\\sigma$ = {sigma}')

ax.legend()
plt.show()
