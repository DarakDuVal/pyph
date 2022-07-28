"""Exercise 2.2, page 67"""

import numpy as np

arr = np.array([[i for i in range(1, 10)]])
print(np.transpose(arr) * arr)
