import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

f = np.array([0.20, 0.50, 0.57, 0.63, 0.67, 0.71, 0.80, 1.00, 1.33])
A = np.array([0.84, 1.42, 1.80, 2.10, 2.22, 2.06, 1.45, 0.64, 0.30])
dA = np.array([0.04, 0.07, 0.09, 0.11, 0.11, 0.10, 0.08, 0.03, 0.02])


def func(f, A0, f0, delta):
    return (A0 * f0 ** 2) / np.sqrt((f ** 2 - f0 ** 2) ** 2 + (delta * f / np.pi) ** 2)


popt, pcov = opt.curve_fit(func, f, A)
print(popt)
print(pcov)

A0, f0, delta = popt
d_A0, d_F0, d_delta = np.sqrt(np.diag(pcov))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel("f [Hz]")
ax.set_ylabel("A [cm]")
ax.grid()

f_fit = np.linspace(np.min(f), np.max(f), 100)
A_fit = func(f_fit, A0, f0, delta)
ax.plot(f_fit, A_fit, '-', zorder=2)
ax.errorbar(f, A, yerr=dA, fmt='.', capsize=2, zorder=3)
plt.show()
