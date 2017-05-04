# -*- coding: utf-8 -*-
"""
Simple demo with multiple subplots.
"""
import numpy as np
import matplotlib.pyplot as plt


x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

ax1=plt.subplot(2, 1, 1)
ax1.plot(x1, y1, 'o-')
ax1.set_title('A tale of 2 subplots')
ax1.set_ylabel('Damped oscillation')

ax2=plt.subplot(2, 1, 2)
ax2.plot(x2, y2, '.-')
ax2.set_xlabel('time (s)')
ax2.set_ylabel('Undamped')

plt.show()