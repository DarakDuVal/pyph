"""Listing 2.10, page 60"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 360, 500)
y1 = np.sin(np.radians(x))
y2 = np.cos(np.radians(x))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_title('Sine and cosine functions')
ax.set_xlabel('Angle [deg]')
ax.set_ylabel('Function value')
ax.set_xlim(0, 360)
ax.set_ylim(-1.1, 1.1)
ax.grid()

ax.plot(x, y1, label='Sine')
ax.plot(x, y2, label='Cosine')
ax.legend()

plt.show()
