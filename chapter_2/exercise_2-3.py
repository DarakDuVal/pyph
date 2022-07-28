"""Exercise 2.3, page 67"""

import numpy as np
import numpy.ma as ma

n = 300

x = np.array([i for i in range(0, n)])
not_prime = np.zeros(n, dtype=bool)

not_prime[0] = True
not_prime[1] = True
for i in range(2, n):
    if not not_prime[i]:
        for j in range(i*2, n, i):
            not_prime[j] = True

print(ma.masked_array(x, mask=not_prime))
