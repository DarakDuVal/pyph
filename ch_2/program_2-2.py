"""Listing_2.2, page 40"""

import math

for angle in range(5, 95, 5):
    x = math.radians(angle)
    error_value = 100 * (x - math.sin(x)) / math.sin(x)

    print(f"Angle: {angle:2} deg, error: {error_value:4.1f} %")
