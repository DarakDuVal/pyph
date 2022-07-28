"""Exercise 3.1 and 3.2, page 88"""

import math
import numpy as np

# T = np.array([2.05, 1.99, 2.06, 1.97, 2.01,
#               2.00, 2.03, 1.97, 2.02, 1.96])

T = np.array([2.05, 1.99, 2.06])

n = T.size

mean = 0
for x in T:
    mean += x
mean /= n

sigma = 0
for x in T:
    sigma += (x-mean)**2
sigma = math.sqrt(sigma / (n-1))

delta_T = sigma / math.sqrt(n)


mean_np = np.mean(T)
sigma_np = np.std(T)
sigma_np_alt = np.std(T, ddof=1)
delta_T_np = sigma / math.sqrt(T.size)


print(f'Mean (loop):                          <T> = {mean:.5f} s')
print(f'Mean (numpy):                         <T> = {mean_np:.5f} s')

print(f'Standard deviation (loop):          sigma = {sigma:.5f} s')
print(f'Standard deviation (numpy):         sigma = {sigma_np:.5f} s')
print(f'Standard deviation (numpy, ddof=1): sigma = {sigma_np_alt:.5f} s')

print(f'Average error (loop):             Delta T = {delta_T:.5f} s')
print(f'Average error (numpy):            Delta T = {delta_T_np:.5f} s')
