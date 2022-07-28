"""Listing 3.3, page 75"""

import math

sigma = 0.5
x_max = 3
dx = 0.01

def f(x):
    a = 1 / (math.sqrt(2 * math.pi) * sigma)
    return a * math.exp(-x**2 / (2 * sigma**2))

x = -x_max
p = 0
while x < x_max:
    p += f(x + dx/2) * dx
    x += dx

print(p)
