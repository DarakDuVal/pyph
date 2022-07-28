"""Exercise 2.4, page 68"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation

x = np.linspace(-370, 730, 1100)
n = 0

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlim(-370, 730)
ax.set_xlabel("Position x")
ax.set_ylim(-1.2, 1.2)
ax.set_ylabel("Fourier transform")
ax.grid()

plot, = ax.plot(x, 0*x)
text = ax.text(0.0, 1.05, '')

def update(n):
    u = 0
    for k in range(0, n):
        u = u + 4./np.pi * np.sin((2*k + 1) * np.radians(x)) / (2*k + 1)

    plot.set_ydata(u)
    text.set_text(f'n = {n}')

    return plot, text

ani = matplotlib.animation.FuncAnimation(fig, update, interval=10, blit=True)
plt.show()
