"""Listing 2.11, page 61"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation

x = np.linspace(0, 20, 500)

omega = 1.      # time-frequency
k = 1.          # spatial frequency
dt = 0.02       # time step

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_ylim(-1.2, 1.2)
ax.set_xlabel('Position x')
ax.set_ylabel('u(x, t)')
ax.grid()

plot, = ax.plot(x, 0 * x)
text = ax.text(0.0, 1.05, '')

def update(n):
    t = n * dt
    u = np.cos(k * x - omega * t)

    plot.set_ydata(u)
    text.set_text(f't = {t:5.2f}')

    return plot, text

ani = matplotlib.animation.FuncAnimation(fig, update, interval=30, blit=True)
plt.show()

# ani = matplotlib.animation.FuncAnimation(fig, update, frames=1000, blit=True)
# ani.save('animated_sine.mpg', fps=30)
