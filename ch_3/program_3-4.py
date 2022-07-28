"""Listing 3.4, page 76"""

import math
import scipy.integrate

sigma = 0.5

def f(x):
    a = 1 / (math.sqrt(2 * math.pi) * sigma)
    return a * math.exp(-x**2 / (2 * sigma**2))

p, err = scipy.integrate.quad(f, -math.inf, math.inf)

print(f'Result of the integration: {p}')
print(f'Numerical error: {err}')
