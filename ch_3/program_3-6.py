"""Listing 3.6, page 79"""

import math
import numpy as np

T = np.array([2.05, 1.99, 2.06, 1.97, 2.01,
              2.00, 2.03, 1.97, 2.02, 1.96])

mean = np.mean(T)
sigma = np.std(T, ddof=1)
delta_T = sigma / math.sqrt(T.size)

print(f'Mean:                   <T> = {mean:.2f} s')
print(f'Standard deviation:   sigma = {sigma:.2f} s')
print(f'Average error:      Delta T = {delta_T:.2f} s')
