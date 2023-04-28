"""Exercise 3.3, page 88"""
import math

import numpy as np
import scipy.integrate as integrate

T = np.array([2.05, 1.99, 2.06, 1.97, 2.01,
              2.00, 2.03, 1.97, 2.02, 1.96])

mean_T = np.mean(T)
sigma_T = np.std(T, ddof=1)

print("<T>=" + str(mean_T))
print("s=" + str(sigma_T))


def gauss(x, mean, sigma):
    a = 1 / (math.sqrt(2 * math.pi) * sigma)
    return a * np.exp(-(x - mean) ** 2 / (2 * sigma ** 2))


lower = 1.95
upper = 2.05
dx = 1e-6
steps = (upper - lower) / dx

print("Integration steps:" + str(steps))

naive_sum = 0
x = lower
while x < upper:
    naive_sum += gauss(x, mean_T, sigma_T) * dx
    x += dx

print("Naive integral: " + str(naive_sum))


quad_sum = integrate.quad(lambda x: gauss(x, mean_T, sigma_T), lower, upper)
print("Scipy.quad: " + str(quad_sum))

print("Delta: " + str(quad_sum[0]-naive_sum))
