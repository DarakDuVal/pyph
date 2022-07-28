"""Exercise 2.5, page 68"""

import numpy as np
import matplotlib.pyplot as plt

x = [0., 0., 1., 2.2, 2.8, 3.8, 4.6, 5.7, 6.4, 7.1, 7.6, 7.9, 7.9]
y = [1., 2.8, 3.3, 3.5, 3.4, 2.7, 2.4, 2.3, 2.1, 1.6, 0.9, 0.5, 0.]

x_shifted = np.roll(x, -1)
y_shifted = np.roll(y, -1)

x_diff = abs(x - x_shifted)
y_sums = y + y_shifted
area = .5 * np.sum(x_diff * y_sums)
print(f'Flowerbed area: {area:5.1f}')

fig = plt.figure()
plt.fill(x, y, facecolor='green')
plt.show()
