"""Listing 3.1, page 72"""

import math

R = 6371e3
m = 5.972e24

V = 4. / 3. * math.pi * R**3
rho = m / V

print(f'Earth\'s average density is {rho/1e3:.3f} g / cm³.')
