# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2.0, 2.0, 10000) # The x-values
sigma = np.linspace(0.4, 1.0, 4) # Some different values of sigma

# Evaluate a Gaussian for each sigma
gaussians = [(2*np.pi*s**2)**-0.5 * np.exp(-0.5*x**2/s**2) for s in sigma]

ax = plt.axes()
for s,y in zip(sigma, gaussians):
    ax.plot(x, y, lw=2, label=r"$\sigma = %3.2f$"%s)

formula = r"$y(x)=\frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{x^2}{2\sigma^2}}$"

ax.text(0.05, 0.80, formula, transform=ax.transAxes, fontsize=20)
ax.set_xlabel(r"$x$", fontsize=18)
ax.set_ylabel(r"$y(x)$", fontsize=18)
ax.legend()
plt.show()