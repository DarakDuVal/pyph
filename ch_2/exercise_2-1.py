#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 2.1, page 67"""


import numpy as np

a21 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b21 = np.array([10, 20, 30, 40])
print(a21+b21)


a22 = a21
b22 = np.array([[10], [20], [30]])
print(a22+b22)


a23 = a21
b23 = np.array([10, 20, 30])
try:
    print(a23+b23)
except ValueError:
    print("Nope, formula (2.3) does not work.")


a24 = np.array([1, 2, 3, 4])
b24 = np.array([[10], [20], [30]])
print(a24+b24)
