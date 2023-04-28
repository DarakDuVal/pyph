import numpy as np
import scipy
import matplotlib.pyplot as plt

v = np.array([5.8, 7.3, 8.9, 10.6, 11.2])
dv = np.array([0.3, 0.3, 0.2, 0.2, 0.1])

F = np.array([0.10, 0.15, 0.22, 0.33, 0.36])
dF = np.array([0.02, 0.02, 0.02, 0.02, 0.02])


def func(v, b, n):
    return b * abs(v) ** n


popt, pcov = scipy.optimize.curve_fit(func, v, F)
print(popt)
print(pcov)

b, n = popt
db, dn = np.sqrt(np.diag(pcov))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel("v [m/s]")
ax.set_ylabel("F [N]")
ax.grid()

v_fit = np.linspace(np.min(v), np.max(v), 500)
F_fit = func(v_fit, b, n)
ax.plot(v_fit, F_fit, '-', zorder=2)

ax.errorbar(v, F, xerr=dv, yerr=dF, fmt='.', capsize=2, zorder=3)

plt.show()
