import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y1, y2, y3 = np.cos(x), np.cos(x + 1), np.cos(x + 2)
titres = ['Signal 1', 'Signal 2', 'Signal 3']

fig, axes = plt.subplots(nrows=3)
fig.tight_layout() #Ajuster en sorte que les subplots remplissent la figure

for ax, y, titre in zip(axes, [y1, y2, y3], titres):
    ax.plot(x, y, color='black')
    ax.set(title=titre)

plt.show()
