"""Listing 2.8, page 49"""

import numpy as np

angle = np.arange(5, 95, 5)
x = np.radians(angle)
error_value = 100 * (x - np.sin(x)) / np.sin(x)

print(angle)
print(error_value)
