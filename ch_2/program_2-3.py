"""Listing 2.3, page 41"""

import math

list_angles = list(range(5, 95, 5))
list_errors = []

for angle in list_angles:
    x = math.radians(angle)
    error_value = 100 * (x - math.sin(x)) / math.sin(x)
    list_errors.append(error_value)

print(list_angles)
print(list_errors)
